from pydantic import BaseModel

from app.schemas.comments import CommentResponse


class ArticleBase(BaseModel):
    title: str
    content: str


class ArticleCreate(ArticleBase):
    ...


class ArticleResponse(ArticleBase):
    id: int | None = None
    user_id: int | None = None
    comments: list[CommentResponse] = []

    class Config:
        orm_mode = True
