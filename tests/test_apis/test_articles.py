from starlette.testclient import TestClient

from tests.test_apis.test_users import test_create_user


def test_create_article(client: TestClient):
    """
    test user ID: 1을 만든 후 테스트를 실행합니다.
    실패할 경우 404 HTTPException이 발생 합니다.
    """
    test_create_user(client)
    response = client.post("/articles/1", json={"title": "test title", "content": "test content"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test title"
    assert data["content"] == "test content"
    assert "id" in data
    article_id = data["id"]

    response = client.get(f"/articles/{article_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["title"] == "test title"
    assert data[0]["content"] == "test content"
    assert data[0]["id"] == article_id


def test_get_articles(client: TestClient):
    response = client.get("/articles")
    print(response.json())


def test_get_articles_by_user_id(client: TestClient):
    test_create_article(client)
    response = client.get("/articles/1")
    print(response.json())


def test_get_article_by_article_id(client: TestClient):
    test_create_article(client)
    response = client.get("/articles/1")
    print(response.json())


def test_update_article(client: TestClient):
    test_create_user(client)
    client.post("/articles/1", json={"title": "test title", "content": "test content"})

    response = client.put("/articles/1", json={"title": "update title", "content": "update content"})
    data = response.json()

    assert data["status code"] == 200
