from __future__ import annotations

import logging

from bs4 import BeautifulSoup
from requests import RequestException, Response
from requests.structures import CaseInsensitiveDict

from .client import Client
from .exceptions import UnreachableError
from .rules.length import length_rule

logger = logging.getLogger(__name__)

EXPECTED_CONTENT_TYPES = (
    "text/html",
    "text/plain",
)
EXPECTED_STATUSES = (200,)


class HackerNewsProxyService:

    RULES: tuple = (length_rule,)

    def get(self, url: str) -> tuple[str | bytes, dict]:
        response = self._get(url)

        headers = self._patch_headers(response.headers)
        if headers["Content-Type"] and any(
            content_type in headers["Content-Type"] for content_type in EXPECTED_CONTENT_TYPES
        ):
            soup = self._make_soup(response.content)
            self._walk(soup)
            return str(soup), headers

        return response.content, headers

    def _get(self, path: str) -> Response:
        try:
            response = Client().get(path)
        except RequestException as e:
            raise UnreachableError from e

        if response.status_code not in EXPECTED_STATUSES:
            raise UnreachableError

        return response

    def _make_soup(self, content: bytes) -> BeautifulSoup:
        return BeautifulSoup(content, features="html.parser")

    def _walk(self, soup: BeautifulSoup) -> BeautifulSoup:
        if body := soup.body:
            for rule in self.RULES:
                candidates = body.find_all(string=rule.condition())
                for candidate in candidates:
                    fixed_element = rule.action(candidate)
                    candidate.replace_with(fixed_element)

        return soup

    def _patch_headers(self, headers: CaseInsensitiveDict[str]) -> dict:
        return {
            "Content-Type": headers.get("Content-Type"),
        }
