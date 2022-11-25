from pydantic import BaseModel


class CommentResponseDTO(BaseModel):
    id: int
    comment: str
    user_id: int
    article_id: int

    class Config:
        orm_mode = True
