from pydantic import BaseModel

from crud.dto.comment import CommentResponseDTO


class ArticleCreateDTO(BaseModel):
    title: str
    content: str


class ArticleUpdateDTO(BaseModel):
    title: str
    content: str


class ArticleResponseDTO(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
