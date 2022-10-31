from pydantic import BaseModel


class CommentBase(BaseModel):
    comment: str


class CommentCreate(CommentBase):
    ...


class CommentResponse(CommentBase):
    id: int
    article_id: int | None = None
    author_id: int | None = None

    class Config:
        orm_mode = True
