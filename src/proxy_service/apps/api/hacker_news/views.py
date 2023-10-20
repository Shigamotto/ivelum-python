from __future__ import annotations

import logging
import typing

from django.http import HttpRequest, HttpResponse
from django.views import View

from proxy_service.apps.hacker_news import HackerNewsProxyService
from proxy_service.apps.hacker_news.exceptions import UnreachableError

logger = logging.getLogger(__name__)

BASE_HTTP_URL = "https://news.ycombinator.com/"


class ProxyView(View):
    def get(self, request: HttpRequest, *args: typing.Any, **kwargs: typing.Any) -> HttpResponse:
        service = HackerNewsProxyService()

        try:
            content, headers = service.get(url=request.get_full_path())
        except UnreachableError:
            return HttpResponse(status=404)

        return HttpResponse(content, headers=headers)
