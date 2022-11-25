from pydantic import BaseModel


class CommentCreateDTO(BaseModel):
    comment: str
