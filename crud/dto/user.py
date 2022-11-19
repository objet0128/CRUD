from pydantic import BaseModel

from crud.dto.article import ArticleResponseDTO
from crud.dto.comment import CommentResponseDTO


class UserCreateDTO(BaseModel):
    email: str
    password: str
    information: str


class UserResponseDTO(BaseModel):
    id: str
    email: str
    information: str
    articles: list[ArticleResponseDTO] = []
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
