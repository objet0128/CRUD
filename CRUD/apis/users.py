from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from CRUD.db.session import get_db
from CRUD.user.domain.users import User
from CRUD.user.schema.users import UserCreate, UserResponse
from CRUD.user.service import users

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    exist_user = users.get_user_by_email(db, email=user.email)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exist")
    return users.create_user(db=db, user=user)


@router.get("/", response_model=list[UserResponse])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[User]:
    user_list = users.get_users(db, skip=skip, limit=limit)
    if user_list is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not exist")
    return user_list


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    return db_user
