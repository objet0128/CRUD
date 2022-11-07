from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import comments
from app.db.session import get_db
from app.models import Comment
from app.schemas.comments import CommentCreate, CommentResponse

router = APIRouter()


@router.post("/", response_model=CommentResponse)
def create_comment(article_id: int, user_id: int, comment: CommentCreate, db: Session = Depends(get_db)) -> Comment:
    return comments.create_comment(article_id=article_id, user_id=user_id, comment=comment, db=db)


@router.get("/{comment_id}", response_model=CommentResponse)
def get_comment_by_author(author_id: int, db: Session = Depends(get_db)) -> list[Comment]:
    return comments.get_comments_by_author(author_id, db)


@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return comments.delete_comment(comment_id, db)
