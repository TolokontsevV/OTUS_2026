import requests
import pytest
from data.Status_codes_pictures import pictures


@pytest.mark.parametrize('picture_url', pictures)
def test_get_pictures(picture_url):
    url = picture_url
    try:
        response = requests.get(url, stream=True)  # stream=True для больших файлов (изображения)
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
        print(response.status_code)
    except AssertionError as e:
        pytest.fail(f"Assertion failed: {e}")
