import logging
import typing
from urllib.parse import urljoin

import requests
from requests import Response

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/39.0.2171.95 Safari/537.36"
)

logger = logging.getLogger(__name__)


class Client(requests.Session):
    BASE_URL = "https://news.ycombinator.com/"

    def __init__(self) -> None:
        super().__init__()
        self.headers.setdefault("User-Agent", DEFAULT_USER_AGENT)

    def _build_url(self, path: str) -> str:
        return urljoin(self.BASE_URL, path)

    def request(  # type: ignore[override]
        self, method: str, url: str, *args: typing.Any, **kwargs: typing.Any
    ) -> Response:
        url = self._build_url(url)
        logger.debug("Make request to %s", url)
        return super().request(method, url, *args, **kwargs)
