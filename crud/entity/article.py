from pydantic import BaseModel

from crud.dto.comment import CommentResponseDTO


class ArticleEntity(BaseModel):
    id: int | None
    title: str | None
    content: str | None
    author_id: int | None
    comments: list[CommentResponseDTO] = []
