import pytest
from django.test import RequestFactory

from zenofewords.views import HomeView


@pytest.mark.django_db
def test_home_view_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_view_uses_correct_template(client):
    response = client.get("/")
    assert "zenofewords/home.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_meta_mixin_populates_context(client):
    response = client.get("/")
    assert response.context["meta_title"] == "Dominik Zen"
    assert response.context["meta_author"] == "Dominik Zen"
    assert response.context["meta_description"] == "Dominik Zen's website"
    assert response.context["meta_image_alt"] == "website logo"
    assert "meta_url" in response.context
