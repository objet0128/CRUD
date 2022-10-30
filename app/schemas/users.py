from pydantic import BaseModel

from app.schemas.articles import Article


class UserBase(BaseModel):
    email: str
    information: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    articles: list[Article] = []

    class Config:
        orm_mode = True
