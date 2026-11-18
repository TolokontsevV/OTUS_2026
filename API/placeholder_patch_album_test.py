import requests


def test_patch_album():
    id = 1
    url = 'https://jsonplaceholder.typicode.com/albums'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.status_code)
    print(len(response.json()))
    print(response.json())

    patch_data = {
        'title': 'Comprehensive testing is impossible.'
    }
    response = requests.patch(f'{url}/{id}', json=patch_data)
    assert response.status_code == 200
    # проверка изменения части данных юзера (статус-код будет всегда 200 и данные
    # т.к. сервис placeholder не позволяет фактически изменять данные
    # и отправляет фиктивные ответы от сервера)
    print(response.status_code)
    assert patch_data['title'] == 'Comprehensive testing is impossible.'\
           in response.json()['title']
