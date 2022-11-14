from pydantic import BaseModel

from app.schemas.articles import ArticleResponse
from app.schemas.comments import CommentResponse


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
