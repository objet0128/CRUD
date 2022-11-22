from pydantic import BaseModel


class CommentCreateDTO(BaseModel):
    comment: str


class CommentResponseDTO(BaseModel):
    id: int
    comment: str
    user_id: int
    article_id: int

    class Config:
        orm_mode = True
