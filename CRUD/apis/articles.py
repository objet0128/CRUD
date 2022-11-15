from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from CRUD.apis.users import get_user
from CRUD.crud import articles
from CRUD.db.session import get_db
from CRUD.models import Article
from CRUD.schemas.articles import ArticleCreate, ArticleResponse

router = APIRouter()


@router.post("/{user_id}/", response_model=ArticleResponse)
def create_article(user_id: int, article: ArticleCreate, db: Session = Depends(get_db)) -> Article:
    if get_user(user_id=id, db=db) is None:
        raise HTTPException(status_code=404, detail="User not exist")
    return articles.create_article(user_id, db, article)


@router.get("/", response_model=list[ArticleResponse])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[Article]:
    db_articles = articles.get_articles(db, skip=skip, limit=limit)
    if db_articles is None:
        raise HTTPException(status_code=404, detail="Articles not exist")
    return db_articles


@router.get("/{user_id}/", response_model=list[ArticleResponse])
def get_articles_by_user_id(user_id: int, db: Session = Depends(get_db)) -> list[Article]:
    db_articles = articles.get_article_by_user_id(user_id=user_id, db=db)
    if db_articles is None:
        raise HTTPException(status_code=404, detail="Articles not exist")
    return db_articles


@router.get("/{article_id}", response_model=ArticleResponse)
def get_article_by_article_id(article_id: int, db: Session = Depends(get_db)) -> Article:
    db_article = articles.get_article_by_article_id(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not exist")
    return db_article


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return articles.delete_article_by_id(article_id=article_id, db=db)


@router.put("/{article_id}")
def update_article(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    return articles.update_article(db=db, article_id=article_id, article=article)
