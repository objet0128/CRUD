from pydantic import BaseModel

from crud.apis.response.comment import CommentResponseDTO


class ArticleSchema(BaseModel):
    id: int | None
    title: str | None
    content: str | None
    author_id: int | None
    comments: list[CommentResponseDTO] = []
