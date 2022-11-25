from crud.apis.request.article import ArticleCreateDTO, ArticleUpdateDTO
from crud.repository.article import ArticleRepository
from crud.schema.article import ArticleSchema


class ArticleService:
    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def create_article(self, author_id: int, request: ArticleCreateDTO) -> ArticleSchema:
        article_entity = ArticleSchema(**request.dict())
        return self.repository.create_article(article=article_entity, author_id=author_id)

    def get_articles(self, skip: int, limit: int) -> list[ArticleSchema]:
        return self.repository.get_articles(skip=skip, limit=limit)

    def get_article(self, article_id: int) -> ArticleSchema:
        return self.repository.get_article(article_id=article_id)

    def get_articles_by_user_id(self, author_id: int) -> list[ArticleSchema]:
        return self.repository.get_articles_by_author(author_id=author_id)

    def delete_article_by_id(self, article_id: int) -> int:
        return self.repository.delete_article_by_id(article_id=article_id)

    def update_article(self, article_id: int, request: ArticleUpdateDTO):
        return self.repository.update_article(article_id=article_id, article=request)
