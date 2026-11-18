import requests


def test_get_dog_header():
    url = 'https://dog.ceo/dog-api/'
    response = requests.get(url)
    assert response.status_code == 200

    headers = {
        'Connection': 'keep-alive',
        'Transfer-Encoding': 'chunked',
        'Content-type': 'application/json'
    }

    response_head = requests.get(url, headers=headers)
    assert headers['Connection'] == response_head.request.headers['Connection'], \
        "Заголовок Connection не совпадает в запросе и ответе"
    assert response_head.request.headers['Transfer-Encoding'] == headers['Transfer-Encoding'], \
        "Заголовок Transfer-Encoding не совпадает в запросе и ответе"
    assert response_head.request.headers['Content-type'] == headers['Content-type'], \
        "Заголовок Content-type не совпадает в запросе и ответе"

    print(response.status_code)
    print(response.headers)
