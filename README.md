# zenofewords

Personal space for hobby projects.

## Stack

- Django, PostgreSQL, gunicorn
- Deno (TypeScript bundling)
- Caddy (reverse proxy, automatic HTTPS)
- GitHub Actions (CI/CD)

## Development

```
uv sync
uv run python manage.py runserver
deno task build:watch
```

### Tests

```
uv run pytest
deno task test
```

## Deployment

Pushes to `main` trigger the GitHub Actions workflow which runs tests and deploys to the droplet via SSH.

For initial droplet setup, see `deploy/droplet-setup.sh`.
