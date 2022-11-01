from pydantic import BaseModel


class CommentBase(BaseModel):
    comment: str


class CommentCreate(CommentBase):
    ...


class CommentResponse(CommentBase):
    id: int
    user_id: int | None = None
    article_id: int | None = None

    class Config:
        orm_mode = True
