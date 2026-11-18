import requests


def test_openbrewery_meta():
    url = 'https://api.openbrewerydb.org/v1/breweries/meta?by_country'
    # проверка запроса по городам Южной Кореи в фильтрации по странам
    response = requests.get(url, params={'by_country': 'south_korea'})
    assert response.status_code == 200
    print(response.status_code)
    print(response.json())

    response = response.text
    assert 'Busan' in response
    assert 'Chungcheongbukdo' in response
    assert 'Daejeon' in response
    assert 'Deagu' in response
    assert 'Gangwondo' in response
    assert 'Gwangju' in response
    assert 'Gyeonggido' in response
    assert 'Gyeongsangbukdo' in response
    assert 'Gyeongsangnamdo' in response
    assert 'Incheon' in response
    assert 'Jejudo' in response
    assert 'Jeollabukdo' in response
    assert 'Jeollanamdo' in response
    assert 'Seoul' in response
