import requests
import pytest
from data.Status_codes_pictures import user_id


@pytest.mark.parametrize('id', user_id)
def test_placeholder_post(id): # изменение данных уже созданного юзера
    user_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    response = requests.get(user_url)
    print(response.status_code)
    assert response.status_code == 200

    update_data = {
        "id": 11,
        "name": 'Igor',
        "username": "Vasya",
        "email": 'IgorT@may.biz',
        "address": {
            "street": "Kulas Dark",
            "suite": "Apt. 655",
            "city": "Vologda",
            "zipcode": "156613",
            "geo": {
                "lat": "37.3159",
                "lng": "-81.1496"
            }
        },
        "phone": "2-770-6487-8031 x56442",
        "website": "https://youtube.com/@tukhlii?si=KltoPUl7hkn3vfmA",
        "company": {
            "name": "RSHB-Intex",
            "catchPhrase": "Single-layered client-server neural-net",
            "bs": "Post application"
        }
    }

    response = requests.put(user_url, json=update_data)
    assert response.status_code == 200
    print(response.json())

    # проверка изменения данных юзера (статус-код будет всегда 200 и данные не изменяются
    # т.к. сервис placeholder не позволяет фактически изменять данные
    # и отправляет фиктивные ответы от сервера)

    response = requests.get(user_url)
    assert response.status_code == 404
    assert response.json() == update_data
    print(response.json())
