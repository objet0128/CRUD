from starlette.testclient import TestClient

from tests.test_apis.test_articles import test_create_article


def test_create_comment(client: TestClient):
    test_create_article(client)
    response = client.post(
        "/comments/?article_id=1&user_id=1", json={"article_id": "1", "user_id": "1", "comment": "this is for test"}
    )
    assert response.status_code == 200, response.text


def test_get_comments_by_author(client: TestClient):
    test_create_comment(client)
    response = client.get("/comments/1?author_id=1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["comment"] == "this is for test"
