import requests


def test_get_dog_all_list():
    url = 'https://dog.ceo/api/breeds/list/all'

    response = requests.get(url)
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict['message'], [1] == {'african': ['wild']}

    print(response.status_code)
    print(response_dict)
