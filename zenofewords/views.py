from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import TemplateView


class MetaMixin(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            "meta_url": f"{self.request.scheme}://{get_current_site(self.request)}",
            "meta_title": "Dominik Zen",
            "meta_author": "Dominik Zen",
            "meta_description": "Dominik Zen's website",
            "meta_image_alt": "website logo",
        }
        context.update(data)
        return context


class HomeView(MetaMixin):
    template_name = "zenofewords/home.html"
