from fastapi import Depends
from sqlalchemy.orm import Session

from app.crud import articles
from app.db.session import get_db
from app.main import app
from app.models import Article
from app.schemas.articles import ArticleCreate, ArticleResponse


@app.post("/article/{user_id}/", response_model=ArticleResponse)
def create_article(user_id: int, article: ArticleCreate, db: Session = Depends(get_db)) -> Article:
    return articles.create_article(user_id, db, article)


@app.get("/articles/", response_model=list[ArticleResponse])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[Article]:
    return articles.get_articles(db, skip=skip, limit=limit)


@app.get("/{user_id}/articles/", response_model=list[ArticleResponse])
def get_articles_by_user_id(user_id: int, db: Session = Depends(get_db)) -> list[Article]:
    return articles.get_article_by_user_id(user_id=user_id, db=db)


@app.delete("/article/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return articles.delete_article_by_id(article_id=article_id, db=db)


@app.put("/article/{article_id}", response_model=ArticleResponse)
def update_article(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    return articles.update_article(db=db, article_id=article_id, article=article)
