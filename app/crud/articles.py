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
