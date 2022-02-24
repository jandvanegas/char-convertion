from pytest import fixture
from fastapi.testclient import TestClient

from aschii_chars.main import app


@fixture(scope="session")
def client():
    yield TestClient(app)


def test_return_correct_number_for_letters_under_h(client):
    payload = ['a']
    response = client.post("/convert", json=payload)
    assert response.status_code == 200
    assert response.json() == [970]


def test_return_correct_number_for_letters_under_B(client):
    payload = ['B']
    response = client.post("/convert", json=payload)
    assert response.status_code == 200
    assert response.json() == [660]


def test_return_correct_number_for_letters_over_h(client):
    payload = ['h']
    response = client.post("/convert", json=payload)
    assert response.status_code == 200
    assert response.json() == [0]


def test_return_correct_number_for_letters_over_H(client):
    payload = ['Z']
    response = client.post("/convert", json=payload)
    assert response.status_code == 200
    assert response.json() == [0]


def test_return_correct_convertion_for_a_list_of_characters(client):
    payload = ["A", "h", "H", "x"]
    response = client.post("/convert", json=payload)
    assert response.status_code == 200
    assert response.json() == [650, 0, 0, 0]

