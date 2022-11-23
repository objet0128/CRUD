from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from crud.db.session import get_db
from crud.dto.comment import CommentCreateDTO, CommentResponseDTO
from crud.repository.article import ArticleRepository
from crud.repository.comment import CommentRepository
from crud.repository.user import UserRepository
from crud.service.article import ArticleService
from crud.service.comment import CommentService
from crud.service.user import UserService

router = APIRouter()


@router.post("/", response_model=CommentResponseDTO, status_code=status.HTTP_201_CREATED)
def create_comment(article_id: int, user_id: int, comment: CommentCreateDTO, db: Session = Depends(get_db)):
    db_user = UserService(UserRepository(db=db)).get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    db_article = ArticleService(ArticleRepository(db=db)).get_article(article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    comment = CommentService(CommentRepository(db=db)).create_comment(
        article_id=article_id, user_id=user_id, request=comment
    )
    return CommentResponseDTO(**comment.dict())


@router.get("/{author_id}", response_model=list[CommentResponseDTO])
def get_comments_by_author(author_id: int, db: Session = Depends(get_db)):
    db_comments = CommentService(CommentRepository(db=db)).get_comments_by_author(author_id=author_id)
    if not db_comments or db_comments is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comments not exist")
    comment_list = [CommentResponseDTO(**comment.dict()) for comment in db_comments]
    return comment_list
