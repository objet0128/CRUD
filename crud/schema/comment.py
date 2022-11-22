from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: int | None
    comment: str | None
    user_id: int | None
    article_id: int | None
