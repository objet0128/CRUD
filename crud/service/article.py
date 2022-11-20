from crud.dto.article import ArticleCreateDTO, ArticleUpdateDTO
from crud.entity.article import ArticleEntity
from crud.repository.article import ArticleRepository


class ArticleService:
    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def create_article(self, author_id: int, request: ArticleCreateDTO) -> ArticleEntity:
        article_entity = ArticleEntity(**request.dict())
        create_article = self.repository.create_article(article=article_entity, author_id=author_id)
        return create_article

    def get_articles(self, skip: int, limit: int) -> list[ArticleEntity]:
        return self.repository.get_articles(skip=skip, limit=limit)

    def get_article(self, article_id: int) -> ArticleEntity:
        return self.repository.get_article(article_id=article_id)

    def get_articles_by_user_id(self, author_id: int) -> list[ArticleEntity]:
        return self.repository.get_articles_by_author(author_id=author_id)

    def delete_article_by_id(self, article_id: int) -> int:
        return self.repository.delete_article_by_id(article_id=article_id)

    def update_article(self, article_id: int, request: ArticleUpdateDTO):
        return self.repository.update_article(article_id=article_id, article=request)
