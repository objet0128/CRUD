from typing import List

from sqlalchemy.orm import Session, joinedload

from crud.db.model.article import Article
from crud.dto.article import ArticleUpdateDTO
from crud.domain.article import Article


class ArticleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_article(self, author_id: int, article: Article) -> Article:
        db_article = Article(**article.dict(exclude={"author_id"}), author_id=author_id)
        self.db.add(db_article)
        self.db.commit()
        self.db.refresh(db_article)
        article = Article(**db_article.__dict__)
        return article

    def get_articles(self, skip: int = 0, limit: int = 100) -> list[Article] | None:
        db_articles = self.db.query(Article).options(joinedload(Article.comments)).offset(skip).limit(limit).all()
        if not db_articles:
            return None
        articles = [Article(**article.__dict__) for article in db_articles]
        return articles

    def get_article(self, article_id: int) -> Article | None:
        db_article = self.db.query(Article).filter(Article.id == article_id).first()
        if db_article is None:
            return None
        article = Article(**db_article.__dict__)
        return article

    def get_articles_by_author(self, author_id: int) -> list[Article] | None:
        db_articles = self.db.query(Article).options(joinedload(Article.comments)).filter(
            Article.author_id == author_id).all()
        if not db_articles:
            return None
        articles = [Article(**article.__dict__) for article in db_articles]
        return articles

    def delete_article_by_id(self, article_id: int):
        article = self.db.query(Article).filter(Article.id == article_id)
        article.delete()
        self.db.commit()

    def update_article(self, article_id: int, article: ArticleUpdateDTO):
        self.db.query(Article).filter(Article.id == article_id).update(article.dict())
        self.db.commit()
        return article
