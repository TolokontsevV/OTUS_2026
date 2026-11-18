import requests


def test_ya_addopt(url, status):
    response = requests.get(f"https://ya.ru/{url}")
    assert response.status_code == int(status)
