from sqlalchemy.orm import Session

from app.models import Article
from app.schemas.articles import ArticleCreate


def create_article(user_id: int, db: Session, article: ArticleCreate) -> Article:
    db_article = Article(**article.dict(), user_id=user_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(db: Session, skip: int = 0, limit: int = 100) -> list[Article]:
    return db.query(Article).offset(skip).limit(limit).all()


def get_article(db: Session, article_id: int) -> Article:
    return db.query(Article).filter(Article.id == article_id).first()


def get_article_by_user_id(db: Session, user_id: int) -> list[Article]:
    return db.query(Article).filter(Article.user_id == user_id).all()


def get_article_by_article_id(db: Session, article_id: int) -> Article:
    return db.query(Article).filter(Article.id == article_id).first()


def delete_article_by_id(article_id: int, db: Session) -> int:
    article = db.query(Article).filter(Article.id == article_id)
    if not article:
        return 0
    article.delete()
    db.commit()
    return 1


def update_article(db: Session, article_id: int, article: ArticleCreate) -> int:
    db_article = db.query(Article).filter(Article.id == article_id)
    if not db_article:
        return 0
    db_article.update(article.dict())
    db.commit()
    return 1
