#!/usr/bin/env bash
# One-time droplet bootstrap — run as root on a fresh Ubuntu 24.04 droplet.
# After running this, clone the repo as the deploy user and create .env.
set -euo pipefail

DEPLOY_USER="deploy"
PROJECT_DIR="/home/$DEPLOY_USER/zenofewords"

# --- System packages ---
apt-get update && apt-get upgrade -y
apt-get install -y git curl postgresql

# --- Caddy ---
apt-get install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' \
  | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' \
  | tee /etc/apt/sources.list.d/caddy-stable.list
apt-get update && apt-get install -y caddy

# --- Deploy user ---
adduser --disabled-password --gecos "" $DEPLOY_USER
mkdir -p /home/$DEPLOY_USER/.ssh
# >>> paste your public key into authorized_keys <<<
# cp /root/.ssh/authorized_keys /home/$DEPLOY_USER/.ssh/authorized_keys
chown -R $DEPLOY_USER:$DEPLOY_USER /home/$DEPLOY_USER/.ssh
chmod 700 /home/$DEPLOY_USER/.ssh

# Allow deploy user to restart its own services without password
cat > /etc/sudoers.d/$DEPLOY_USER << 'SUDOERS'
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart zenofewords
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart caddy
SUDOERS

# --- PostgreSQL database ---
sudo -u postgres createuser $DEPLOY_USER
sudo -u postgres createdb -O $DEPLOY_USER zenofewords

# --- uv (Python package manager) ---
su - $DEPLOY_USER -c "curl -LsSf https://astral.sh/uv/install.sh | sh"

# --- Deno ---
su - $DEPLOY_USER -c "curl -fsSL https://deno.land/install.sh | sh"

# --- Clone repo (as deploy user) ---
su - $DEPLOY_USER -c "git clone git@github.com:zenofewords/zenofewords.git $PROJECT_DIR"

echo ""
echo "Done. Next steps:"
echo "  1. Create $PROJECT_DIR/.env (see .env.example)"
echo "  2. Copy Caddyfile to /etc/caddy/Caddyfile"
echo "  3. Copy systemd unit to /etc/systemd/system/zenofewords.service"
echo "  4. Run: systemctl daemon-reload && systemctl enable --now zenofewords caddy"
echo "  5. Run initial migration: cd $PROJECT_DIR && uv run python manage.py migrate"
