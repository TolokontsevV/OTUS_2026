import requests
from data.Status_codes_pictures import search
import pytest


@pytest.mark.parametrize('search', search)
def test_openbrewery_search(search):
    url = f'https://api.openbrewerydb.org/v1/breweries/search?query=/{search}'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.status_code)

    found_data = response.text
    assert search in found_data
    print(search, found_data)
