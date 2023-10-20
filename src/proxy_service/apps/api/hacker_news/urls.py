from django.urls import re_path

from .views import ProxyView

app_name = "apps-hacker-news"
urlpatterns = [re_path(".*", ProxyView.as_view(), name="call")]
