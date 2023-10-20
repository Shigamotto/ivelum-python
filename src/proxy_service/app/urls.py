from django.urls import include, path

urlpatterns = [
    path("", include("proxy_service.apps.api.hacker_news.urls")),
]
