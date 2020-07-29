from django.contrib import admin
from django.urls import path

from zenofewords.views import (
    ContactView,
    HomepageView,
    PersonalView,
    ProfessionalView,
    RamblingsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view(), name='contact'),
    path('personal/', PersonalView.as_view(), name='personal'),
    path('professional/', ProfessionalView.as_view(), name='professional'),
    path('ramblings/', RamblingsView.as_view(), name='ramblings'),
    path('', HomepageView.as_view(), name='homepage'),
]
