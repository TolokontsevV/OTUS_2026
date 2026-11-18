import requests
import pytest
from data.Status_codes_pictures import filtered_params


@pytest.mark.parametrize('filter_by', filtered_params)
def test_openbrewery_list(filter_by):
    url = f'https://api.openbrewerydb.org/v1/breweries?/{filter_by}'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.status_code)
    print(response.json())
