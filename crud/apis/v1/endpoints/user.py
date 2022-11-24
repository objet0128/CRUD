from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from crud.db.session import get_db
from crud.dto.user import UserCreateDTO, UserResponseDTO
from crud.repository.user import UserRepository
from crud.service.user import UserService

router = APIRouter()


@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    exist_user = UserService(UserRepository(db=db)).get_user_by_email(email=user.email)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exist")
    user = UserService(UserRepository(db=db)).create_user(request=user)
    user_response = UserResponseDTO(**user.dict())
    return user_response


@router.get("/", response_model=list[UserResponseDTO])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_list = UserService(UserRepository(db=db)).get_user_list(skip=skip, limit=limit)
    if not user_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not exist")
    user_list_response = [UserResponseDTO(**user.dict()) for user in user_list]
    return user_list_response


@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserService(UserRepository(db=db)).get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    user = UserResponseDTO(**db_user.dict())
    return user
