import requests
import pytest


def test_placeholder_post(): # создание нового пользвателя
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    print(response.status_code)
    assert response.status_code == 200

    body = {
        "id": 11,
        "name": "Vasily Tolokontsev",
        "username": "Vasya",
        "email": "TolokontsevV@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Cherepovets",
            "zipcode": "162622",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "https://youtube.com/@tukhlii?si=KltoPUl7hkn3vfmA",
        "company": {
            "name": "R-Style",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "Bank application"
        }
    }

    try:
        response = requests.post(url, json=body)
        assert response.status_code == 201, f"Ожидался статус 201 Created, но получен {response.status_code}"
    except AssertionError as e:
        pytest.fail(f"Assertion failed: {e}")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred: {e}")
    print(response.json())
    print(response.status_code)

    # проверка созданного пользователя (статус-код будет всегда 404,
    # т.к. сервис placeholder не позволяет фактически создавать
    # и отправляет фиктивные ответы от сервера)
    response_json = response.json()
    user_id = response_json.get('id')
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    print('id user =', user_id, ', status code', response.status_code)
    # assert response_json [1] ['name'] == 'Vasily Tolokontsev'
