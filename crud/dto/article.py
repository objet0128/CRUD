from pydantic import BaseModel

from crud.dto.comment import CommentResponseDTO


class ArticleCreateDTO(BaseModel):
    title: str
    content: str


class ArticleUpdateDTO(BaseModel):
    title: str
    content: str


class ArticleResponseDTO(BaseModel):
    id: int | None = None
    author_id: int | None = None
    title: str
    content: str
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
