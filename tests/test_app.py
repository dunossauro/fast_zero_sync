from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.NOT_FOUND  # assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
