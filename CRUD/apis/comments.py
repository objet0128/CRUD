from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from CRUD.article.service.articles import get_article
from CRUD.comment.domain.comments import Comment
from CRUD.comment.schema.comments import CommentCreate, CommentResponse
from CRUD.comment.service import comments
from CRUD.db.session import get_db
from CRUD.user.service.users import get_user

router = APIRouter()


@router.post("/", response_model=CommentResponse)
def create_comment(article_id: int, user_id: int, comment: CommentCreate, db: Session = Depends(get_db)) -> Comment:
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    db_article = get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not exist")
    return comments.create_comment(article_id=article_id, user_id=user_id, comment=comment, db=db)


@router.get("/{comment_id}", response_model=list[CommentResponse])
def get_comments_by_author(author_id: int, db: Session = Depends(get_db)) -> list[Comment]:
    db_comments = comments.get_comments_by_author(author_id, db)
    if db_comments is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comments not exist")
    return db_comments
