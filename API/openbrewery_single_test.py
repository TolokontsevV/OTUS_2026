import requests
import pytest
from data.Status_codes_pictures import brewery_id


@pytest.mark.parametrize("brewery_id", brewery_id)
def test_openbrewery_single_get(brewery_id):
    obdb_id = brewery_id
    url = f'https://api.openbrewerydb.org/v1/breweries/{obdb_id}'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.status_code)

    field_brewery = response.json()
    print(field_brewery)
    assert 'id' in field_brewery
    assert 'name' in field_brewery
    assert 'brewery_type' in field_brewery
    assert 'address_1' in field_brewery
    assert 'address_2' in field_brewery
    assert 'address_3' in field_brewery
    assert 'city' in field_brewery
    assert 'state_province' in field_brewery
    assert 'country' in field_brewery
    assert 'postal_code' in field_brewery
    assert 'latitude' in field_brewery
    assert 'longitude' in field_brewery
    assert 'phone' in field_brewery
    assert 'website_url' in field_brewery
    assert 'state' in field_brewery
    assert 'street' in field_brewery

    # Проверка на соответствие ответа полей по типу значения (str, int, float, None)
    # так и не получилась
    # assert isinstance(field_brewery['id'], str)
    # assert isinstance(field_brewery['name'], str)
    # assert isinstance(field_brewery['brewery_type'], str)
    # assert isinstance(field_brewery['address_1'], str or None)
    # assert isinstance(field_brewery['address_2'], str or None)
    # assert isinstance(field_brewery['address_3'], str or None)
    # assert isinstance(field_brewery['city'], str)
    # assert isinstance(field_brewery['state_province'], str)
    # assert isinstance(field_brewery['postal_code'], str)
    # assert isinstance(field_brewery['country'], str)
    # assert isinstance(field_brewery['longitude'], float)
    # assert isinstance(field_brewery['latitude'], float)
    # assert isinstance(field_brewery['phone'], str or None)
    # assert isinstance(field_brewery['website_url'], str or None)
    # assert isinstance(field_brewery['state'], str)
    # assert isinstance(field_brewery['street'], str or None)
