import requests


def test_comment_del():
    url_comment = 'https://jsonplaceholder.typicode.com/comments/'
    id_comment = 10
    url = f"{url_comment}/{id_comment}"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

    del_comment = requests.delete(url)
    assert response.status_code in [200, 204]
    assert del_comment.json() == {}
    print(response.status_code)

    # проверка удаленного комментария (статус-код будет всегда 200,
    # т.к. сервис placeholder не позволяет фактически создавать/удалять
    # и отправляет фиктивные ответы от сервера)
    response = requests.get(url)
    assert response.status_code == 404
    print(response.status_code)
