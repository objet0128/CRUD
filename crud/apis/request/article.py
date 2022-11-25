from pydantic import BaseModel


class ArticleCreateDTO(BaseModel):
    title: str
    content: str


class ArticleUpdateDTO(BaseModel):
    title: str
    content: str
