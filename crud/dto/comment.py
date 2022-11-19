from pydantic import BaseModel


class CommentCreateDTO(BaseModel):
    comment: str


class CommentResponseDTO(BaseModel):
    id: int
    comment: str
    user_id: int | None
    article_id: int | None

    class Config:
        orm_mode = True
