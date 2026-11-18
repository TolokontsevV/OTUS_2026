import requests


def test_random_img():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200

    response_random = requests.get('https://dog.ceo/api/breeds/image/random')
    response_dict = response_random.json()
    print(response_dict)
    assert response_dict['status'], [] == {'success'}
