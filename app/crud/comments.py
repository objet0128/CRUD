from sqlalchemy.orm import Session

from app.models import Comment
from app.schemas.comments import CommentCreate


def create_comment(article_id: int, user_id: int, comment: CommentCreate, db: Session) -> Comment:
    comment = Comment(**comment.dict(), article_id=article_id, user_id=user_id)
    db.add(comment)
    db.commit()
    return comment


def get_comments_by_author(author_id: int, db: Session) -> list[Comment]:
    comments = db.query(Comment).filter(Comment.author_id == author_id).all()
    return comments


def delete_comment(comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id)
    comment.delete()
    db.commit()
    return 1
