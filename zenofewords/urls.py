from django.contrib import admin
from django.urls import path

from zenofewords.views import (
    ContactView,
    HomeView,
    BioView,
    WorkView,
    ThoughtsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view(), name='contact'),
    path('bio/', BioView.as_view(), name='bio'),
    path('work/', WorkView.as_view(), name='work'),
    path('thoughts/', ThoughtsView.as_view(), name='thoughts'),
    path('', HomeView.as_view(), name='home'),
]
