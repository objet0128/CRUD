from pydantic import BaseModel

from crud.apis.response.article import ArticleResponseDTO
from crud.apis.response.comment import CommentResponseDTO


class UserResponseDTO(BaseModel):
    id: str
    email: str
    information: str
    articles: list[ArticleResponseDTO] = []
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
