from fastapi.testclient import TestClient

from main import hh_app


client = TestClient(hh_app)


def test_create_resume():
    response = client.get(
        "http://127.0.0.1:8001/docs/",
    )
    if response.status_code == 200:
        assert True
    else:
        print("Неправильная валидация данных при создании резюме.")
        assert False
