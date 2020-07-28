from django.contrib import admin
from django.urls import path

from zenofewords.views import (
    HomepageView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
]
