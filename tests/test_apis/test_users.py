from fastapi.testclient import TestClient


def test_get_user_list(client: TestClient):
    response = client.get("/users/")
    print(response.json())


def test_create_user(client: TestClient):
    """
    user를 생성한다.
    실패시 HTTPException 400 발생
    """
    response = client.post("/users", json={"email": "test@gmail.com", "information": "string", "password": "string"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "test@gmail.com"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "test@gmail.com"
    assert data["id"] == user_id
