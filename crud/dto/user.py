import re

from pydantic import BaseModel, validator

from crud.dto.article import ArticleResponseDTO
from crud.dto.comment import CommentResponseDTO


class UserCreateDTO(BaseModel):
    email: str
    password: str
    information: str

    @validator("email")
    def validate_email(cls, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Only email please")
        else:
            return value


class UserResponseDTO(BaseModel):
    id: str
    email: str
    information: str
    articles: list[ArticleResponseDTO] = []
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
