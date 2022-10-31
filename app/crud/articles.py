from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.articles import ArticleCreate, Article


def create_article(db: Session, article: ArticleCreate) -> Article:
    db_article = Article(title=article.title, content=article.content)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(db: Session, skip: int = 0, offset: int = 100) -> list[Article]:
    return db.query(Article).offset(skip).limit(offset).all()


def get_article(db: Session, article_id: int) -> Article:
    return db.query(Article).filter(Article.id == article_id).first()


def delete_article_by_id(id: int, db: Session) -> int:
    article = db.query(Article).filter(Article.id == id)
    if not article:
        return 0
    article.delete()
    db.commit()
    return 1


def update_article(db: Session, article_id: int, article: ArticleCreate) -> int:
    db_article = db.query(Article).filter(Article.id == article_id).get()
    if not db_article:
        return 0
    db_article.update(article.__dict__)
    db.commit()
    return 1
