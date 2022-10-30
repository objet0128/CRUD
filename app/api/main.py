import uvicorn as uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import articles, users
from app.db.base_class import Base
from app.db.session import engine, get_db
from app.schemas.articles import Article
from app.schemas.users import User, UserCreate


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    exist_user = users.get_user_by_email(db, email=user.email)
    if exist_user:
        raise HTTPException(status_code=400, detail="Already exist")
    return users.create_user(db=db, user=user)


@app.get("/users/", response_model=list[User])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[User]:
    user_list = users.get_users(db, skip=skip, limit=limit)
    return user_list


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Not exist")
    return db_user


@app.get("/articles/", response_model=list[Article])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[Article]:
    articles.get_articles(db, skip=skip, limit=limit)


if __name__ == "__main__":
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)
