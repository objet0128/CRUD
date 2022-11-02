import uvicorn as uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.crud import articles, comments, users
from app.db.init_db import init_db
from app.db.session import get_db
from app.models import Article, Comment, User
from app.schemas.articles import ArticleCreate, ArticleResponse
from app.schemas.comments import CommentCreate, CommentResponse
from app.schemas.users import UserCreate, UserResponse

init_db()
app = FastAPI()


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    exist_user = users.get_user_by_email(db, email=user.email)
    if exist_user:
        raise HTTPException(status_code=400, detail="Already exist")
    return users.create_user(db=db, user=user)


@app.get("/users/", response_model=list[UserResponse])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[User]:
    user_list = users.get_users(db, skip=skip, limit=limit)
    return user_list


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Not exist")
    return db_user


@app.post("/article/{user_id}/", response_model=ArticleResponse)
def create_article(user_id: int, article: ArticleCreate, db: Session = Depends(get_db)) -> Article:
    return articles.create_article(user_id, db, article)


@app.get("/articles/", response_model=list[ArticleResponse])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[Article]:
    return articles.get_articles(db, skip=skip, limit=limit)


@app.get("/{user_id}/articles/", response_model=list[ArticleResponse])
def get_articles_by_user_id(user_id: int, db: Session = Depends(get_db)) -> list[Article]:
    return articles.get_article_by_user_id(user_id=user_id, db=db)


@app.delete("/article/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return articles.delete_article_by_id(article_id=article_id, db=db)


@app.put("/article/{article_id}", response_model=ArticleResponse)
def update_article(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    return articles.update_article(db=db, article_id=article_id, article=article)


@app.post("/comment", response_model=CommentResponse)
def create_comment(article_id: int, user_id: int, comment: CommentCreate, db: Session = Depends(get_db)) -> Comment:
    return comments.create_comment(article_id=article_id, user_id=user_id, comment=comment, db=db)


@app.get("/comment/{comment_id}", response_model=CommentResponse)
def get_comment_by_author(author_id: int, db: Session = Depends(get_db)) -> list[Comment]:
    return comments.get_comments_by_author(author_id, db)


@app.delete("/comment/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return comments.delete_comment(comment_id, db)


if __name__ == "__main__":
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)
