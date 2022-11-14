from starlette.testclient import TestClient


def test_create_article(client: TestClient):
    response = client.post("/articles/1/", json={"title": "test title", "content": "test content"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test title"
    assert data["content"] == "test content"
    assert "id" in data
    article_id = data["id"]

    response = client.get(f"/articles/{article_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test title"
    assert data["content"] == "test content"
    assert data["id"] == article_id


def test_get_articles(client: TestClient):
    response = client.get("/articles/")
    print(response.json())


def test_get_articles_by_user_id(client: TestClient):
    response = client.get("/articles/1/")
    print(response.json())
