from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str


class ArticleCreate(ArticleBase):
    ...


class ArticleResponse(ArticleBase):
    id: int | None = None
    user_id: int | None = None

    class Config:
        orm_mode = True
