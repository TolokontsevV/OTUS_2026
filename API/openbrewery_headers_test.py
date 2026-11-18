import requests


def test_openbrewery_headers_capital_insensivity():
    response = requests.get("https://openbrewerydb.org")
    print(response.status_code)
    assert response.status_code == 200

    for header_name, header_value in response.headers.items():
        print(f"{header_name}: {header_value}")

    assert response.headers['Content-Type'] == "text/html"
    assert response.headers['content-type'] == "text/html"
