from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import articles
from app.db.session import get_db
from app.models import Article
from app.schemas.articles import ArticleCreate, ArticleResponse

router = APIRouter()


@router.post("/{user_id}/", response_model=ArticleResponse)
def create_article(user_id: int, article: ArticleCreate, db: Session = Depends(get_db)) -> Article:
    return articles.create_article(user_id, db, article)


@router.get("/", response_model=list[ArticleResponse])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[Article]:
    return articles.get_articles(db, skip=skip, limit=limit)


@router.get("/{user_id}/", response_model=list[ArticleResponse])
def get_articles_by_user_id(user_id: int, db: Session = Depends(get_db)) -> list[Article]:
    return articles.get_article_by_user_id(user_id=user_id, db=db)


@router.get("/{article_id}", response_model=ArticleResponse)
def get_article_by_article_id(article_id: int, db: Session = Depends(get_db)) -> Article:
    return articles.get_article_by_article_id(db, article_id)


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return articles.delete_article_by_id(article_id=article_id, db=db)


@router.put("/{article_id}")
def update_article(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    return articles.update_article(db=db, article_id=article_id, article=article)
