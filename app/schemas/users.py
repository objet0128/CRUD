from pydantic import BaseModel

from app.schemas.articles import ArticleResponse


class UserBase(BaseModel):
    email: str
    information: str | None = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    articles: list[ArticleResponse] = []

    class Config:
        orm_mode = True
