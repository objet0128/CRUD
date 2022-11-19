from pydantic import BaseModel


class CommentEntity(BaseModel):
    id: int | None
    comment: str
    user_id: int | None
    article_id: int | None
