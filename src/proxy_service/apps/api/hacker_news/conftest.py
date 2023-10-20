import pytest


@pytest.fixture
def hacker_news_response():
    return b"<html><head></head><body>String to patch with punctuation markss.</body></html>\n"
