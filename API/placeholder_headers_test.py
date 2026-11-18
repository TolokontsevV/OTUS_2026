import requests


def test_headers(): # проверка Headers
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.status_code)

    for header_name, header_value in response.headers.items():
        print(f"{header_name}: {header_value}")

    assert response.headers['Content-Type'] == "text/html; charset=UTF-8"
    print(response.headers['Content-Type'])
