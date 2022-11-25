from pydantic import BaseModel

from crud.apis.response.comment import CommentResponseDTO


class ArticleResponseDTO(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    comments: list[CommentResponseDTO] = []

    class Config:
        orm_mode = True
