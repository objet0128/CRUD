from sqlalchemy.orm import Session

from crud.db.model.comment import Comment
from crud.domain.comment import Comment


class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, article_id: int, user_id: int, comment: Comment) -> Comment:
        db_comment = Comment(**comment.dict(exclude={"article_id", "user_id"}), article_id=article_id, user_id=user_id)
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        comment = Comment(**db_comment.__dict__)
        return comment

    def get_comments_by_author(self, author_id: int) -> list[Comment]:
        db_comments = self.db.query(Comment).filter(Comment.user_id == author_id).all()
        comments = [Comment(**comment.__dict__) for comment in db_comments]
        return comments
