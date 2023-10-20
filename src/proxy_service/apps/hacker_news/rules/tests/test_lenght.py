import pytest

from proxy_service.apps.hacker_news.rules.length import length_condition_action


@pytest.mark.parametrize(
    "input_string, expected",
    [
        pytest.param("", "", id="empty"),
        pytest.param("Str", "Str", id="short"),
        pytest.param("Strings", "Strings", id="long"),
        pytest.param("String", "String™", id="match"),
        pytest.param("String:", "String™:", id="punctuation"),
        pytest.param(" String ", " String™ ", id="space"),
    ],
)
def test_action(input_string, expected):
    result = length_condition_action(input_string)  # Act

    assert result == expected
