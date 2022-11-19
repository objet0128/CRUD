from sqlalchemy.orm import Session

from crud.db.model.comment import Comment
from crud.entity.comment import CommentEntity


class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, article_id: int, user_id: int, comment: CommentEntity) -> CommentEntity:
        db_comment = Comment(**comment.dict(exclude={"article_id", "user_id"}), article_id=article_id, user_id=user_id)
        print(db_comment.__dict__)
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        comment = CommentEntity(**db_comment.__dict__)
        return comment

    def get_comments_by_author(self, author_id: int) -> list[CommentEntity]:
        db_comments = self.db.query(Comment).filter(Comment.user_id == author_id).all()
        comments = [CommentEntity(**comment.__dict__) for comment in db_comments]
        return comments
