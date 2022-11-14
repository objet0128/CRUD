from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import comments
from app.db.session import get_db
from app.models import Comment
from app.schemas.comments import CommentCreate, CommentResponse

router = APIRouter()


@router.post("/", response_model=CommentResponse)
def create_comment(article_id: int, user_id: int, comment: CommentCreate, db: Session = Depends(get_db)) -> Comment:
    return comments.create_comment(article_id=article_id, user_id=user_id, comment=comment, db=db)


@router.get("/{comment_id}", response_model=list[CommentResponse])
def get_comments_by_author(author_id: int, db: Session = Depends(get_db)) -> list[Comment]:
    db_comments = comments.get_comments_by_author(author_id, db)
    if db_comments is None:
        raise HTTPException(status_code=404, detail="Comments not exist")
    return db_comments


@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return comments.delete_comment(comment_id, db)
