from django.contrib import admin
from django.urls import path

from zenofewords.views import HomeView, RobotsTxtView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("robots.txt", RobotsTxtView.as_view(), name="robots-txt"),
    path("", HomeView.as_view(), name="home"),
]
