from django.views.generic import TemplateView


class MetaMixin(TemplateView):
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


class ContactView(MetaMixin):
    template_name = 'zenofewords/contact.html'


class PersonalView(MetaMixin):
    template_name = 'zenofewords/personal.html'


class ProfessionalView(MetaMixin):
    template_name = 'zenofewords/professional.html'


class RamblingsView(MetaMixin):
    template_name = 'zenofewords/ramblings.html'


class HomepageView(MetaMixin):
    template_name = 'zenofewords/homepage.html'
