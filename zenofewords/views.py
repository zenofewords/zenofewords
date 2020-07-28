from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'zenofewords/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            'meta_url': 'https://dominikzen.com',
            'meta_title': 'Dominik Zen',
            'meta_author': 'Dominik Zen',
            'meta_description': 'Dominik Zen\'s personal website',
            'meta_image_alt': 'website logo',
        }
        context.update(data)
        return context
