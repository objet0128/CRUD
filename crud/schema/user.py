from pydantic import BaseModel

from crud.apis.response.article import ArticleResponseDTO
from crud.apis.response.comment import CommentResponseDTO


class UserSchema(BaseModel):
    id: int | None
    password: str | None
    email: str | None
    information: str | None
    comments: list[CommentResponseDTO] = []
    articles: list[ArticleResponseDTO] = []
