from requests.exceptions import ConnectionError


def test_response(client, responses, hacker_news_response):
    responses.add(method=responses.GET, url="https://news.ycombinator.com/item?id=13713480", body=hacker_news_response)

    response = client.get("/item?id=13713480")  # Act

    assert response.status_code == 200
    assert response.content.decode() == (
        "<html><head></head><body>String™ to patch with punctuation markss™.</body></html>\n"
    )


def test_response_unreachable(client, responses):
    responses.add(method=responses.GET, url="https://news.ycombinator.com/item?id=13713480", status=404)

    response = client.get("/item?id=13713480")  # Act

    assert response.status_code == 404


def test_response_unavailable_host(client, responses):
    responses.add(method=responses.GET, url="https://news.ycombinator.com/item?id=13713480", body=ConnectionError())

    response = client.get("/item?id=13713480")  # Act

    assert response.status_code == 404


def test_response_unavailable_content_type(client, responses):
    responses.add(
        method=responses.GET,
        url="https://news.ycombinator.com/item?id=13713480",
        headers={"Content-Type": "application/json"},
        json={"data": "String to patch"},
    )

    response = client.get("/item?id=13713480")  # Act

    assert response.status_code == 200
    assert response.content == b'{"data": "String to patch"}'
