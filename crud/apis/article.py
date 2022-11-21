from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from crud.db.session import get_db
from crud.dto.article import (ArticleCreateDTO, ArticleResponseDTO,
                              ArticleUpdateDTO)
from crud.repository.article import ArticleRepository
from crud.repository.user import UserRepository
from crud.service.article import ArticleService
from crud.service.user import UserService

router = APIRouter()


@router.post("/{author_id}", response_model=ArticleResponseDTO)
def create_article(author_id: int, request: ArticleCreateDTO, db: Session = Depends(get_db)):
    db_user = UserService(UserRepository(db=db)).get_user(user_id=author_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
        # return JSONResponse(status_code=404, content="User not exist")
    article = ArticleService(ArticleRepository(db=db)).create_article(author_id=author_id, request=request)
    return ArticleResponseDTO(**article.dict())


@router.get("/", response_model=list[ArticleResponseDTO])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_articles = ArticleService(ArticleRepository(db=db)).get_articles(skip=skip, limit=limit)
    if not db_articles or db_articles is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Articles not exist")
    article_list = [ArticleResponseDTO(**article.dict()) for article in db_articles]
    return article_list


@router.get("/{author_id}", response_model=list[ArticleResponseDTO])
def get_articles_by_author(author_id: int, db: Session = Depends(get_db)):
    db_articles = ArticleService(ArticleRepository(db=db)).get_articles_by_user_id(author_id=author_id)
    if not db_articles or db_articles is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Articles not exist")
    article_list = [ArticleResponseDTO(**article.dict()) for article in db_articles]
    return article_list


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = ArticleService(ArticleRepository(db=db)).get_article(article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    else:
        ArticleService(ArticleRepository(db=db)).delete_article_by_id(article_id=article_id)
    return {"status code": status.HTTP_200_OK}


@router.put("/{article_id}")
def update_article(article_id: int, article: ArticleUpdateDTO, db: Session = Depends(get_db)):
    db_article = ArticleService(ArticleRepository(db=db)).get_article(article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    updated_article = ArticleService(ArticleRepository(db=db)).update_article(article_id=article_id, request=article)
    return {"status code": status.HTTP_200_OK, "updated_article": updated_article}
