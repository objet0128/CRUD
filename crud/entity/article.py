from pydantic import BaseModel


class ArticleEntity(BaseModel):
    id: int | None
    title: str | None
    content: str | None
    user_id: int | None
