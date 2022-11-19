from pydantic import BaseModel

from crud.dto.article import ArticleResponseDTO
from crud.dto.comment import CommentResponseDTO


class UserEntity(BaseModel):
    id: int | None
    password: str
    email: str | None
    information: str | None
    comments: list[CommentResponseDTO] = []
    articles: list[ArticleResponseDTO] = []
