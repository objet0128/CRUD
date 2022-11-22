from pydantic import BaseModel

from crud.dto.article import ArticleResponseDTO
from crud.dto.comment import CommentResponseDTO


class UserSchema(BaseModel):
    id: int | None
    password: str | None
    email: str | None
    information: str | None
    comments: list[CommentResponseDTO] = []
    articles: list[ArticleResponseDTO] = []
