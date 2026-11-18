import requests
import pytest
from data.Status_codes_pictures import STATUS_CODE


@pytest.mark.parametrize('status_code, codes', STATUS_CODE)
def test_get_dog(status_code, codes):
    response = requests.get('https://dog.ceo/dog-api/')

    assert response.status_code == codes, f"Expected {codes}, but got {response.status_code}"
    assert 'Dog' in response.text

    print(response.status_code)
    print('Dog in response, gav-gav!')
