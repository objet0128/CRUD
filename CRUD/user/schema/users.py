from pydantic import BaseModel

from CRUD.article.schema.articles import ArticleResponse
from CRUD.comment.schema.comments import CommentResponse


class UserBase(BaseModel):
    email: str | None = None
    information: str | None = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    articles: list[ArticleResponse] = []
    comments: list[CommentResponse] = []

    class Config:
        orm_mode = True
