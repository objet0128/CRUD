from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from CRUD.article.domain.articles import Article
from CRUD.article.schema.articles import ArticleCreate, ArticleResponse
from CRUD.article.service import articles
from CRUD.article.service.articles import get_article
from CRUD.db.session import get_db
from CRUD.user.service.users import get_user

router = APIRouter()


@router.post("/{user_id}", response_model=ArticleResponse)
def create_article(user_id: int, article: ArticleCreate, db: Session = Depends(get_db)) -> Article:
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    return articles.create_article(user_id, db, article)


@router.get("/", response_model=list[ArticleResponse])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[Article]:
    db_articles = articles.get_articles(db, skip=skip, limit=limit)
    if db_articles is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Articles not exist")
    return db_articles


@router.get("/{user_id}", response_model=list[ArticleResponse])
def get_articles_by_user_id(user_id: int, db: Session = Depends(get_db)) -> list[Article]:
    db_articles = articles.get_article_by_user_id(user_id=user_id, db=db)
    if db_articles is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Articles not exist")
    return db_articles


@router.get("/{article_id}", response_model=ArticleResponse)
def get_article_by_article_id(article_id: int, db: Session = Depends(get_db)) -> Article:
    db_article = articles.get_article_by_article_id(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    return db_article


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    else:
        articles.delete_article_by_id(article_id=article_id, db=db)
    return {"status code": status.HTTP_200_OK}


@router.put("/{article_id}")
def update_article(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    else:
        update_article = articles.update_article(db=db, article_id=article_id, article=article)
    return {"status code": status.HTTP_200_OK, "updated_article": update_article}
