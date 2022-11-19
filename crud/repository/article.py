from sqlalchemy.orm import Session

from crud.db.model.articles import Article
from crud.dto.article import ArticleUpdateDTO
from crud.entity.article import ArticleEntity


class ArticleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_article(self, user_id: int, article: ArticleEntity) -> ArticleEntity:
        db_article = Article(**article.dict(exclude={"user_id"}), user_id=user_id)
        self.db.add(db_article)
        self.db.commit()
        self.db.refresh(db_article)
        article = ArticleEntity(**db_article.__dict__)
        return article

    def get_articles(self, skip: int = 0, limit: int = 100) -> list[ArticleEntity]:
        db_articles = self.db.query(Article).offset(skip).limit(limit).all()
        articles = [ArticleEntity(**article.__dict__) for article in db_articles]
        return articles

    def get_article(self, article_id: int) -> ArticleEntity | None:
        db_article = self.db.query(Article).filter(Article.id == article_id).first()
        if db_article is None:
            return
        article = ArticleEntity(**db_article.__dict__)
        return article

    def get_articles_by_user_id(self, user_id: int) -> list[ArticleEntity]:
        db_articles = self.db.query(Article).filter(Article.user_id == user_id).all()
        articles = [ArticleEntity(**article.__dict__) for article in db_articles]
        return articles

    def delete_article_by_id(self, article_id: int):
        article = self.db.query(Article).filter(Article.id == article_id)
        article.delete()
        self.db.commit()

    def update_article(self, article_id: int, article: ArticleUpdateDTO):
        self.db.query(Article).filter(Article.id == article_id).update(article.dict())
        self.db.commit()
        return article
