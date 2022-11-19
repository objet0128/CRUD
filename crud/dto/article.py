from pydantic import BaseModel

from crud.dto.comment import CommentResponseDTO


class ArticleCreateDTO(BaseModel):
    title: str
    content: str


class ArticleUpdateDTO(BaseModel):
    title: str
    content: str


class ArticleResponseDTO(BaseModel):
    id: str | None = None
    user_id: int | None = None
    content: str
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
