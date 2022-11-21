from typing import List

from sqlalchemy.orm import Session

from crud.db.model.user import User
from crud.domain.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> User:
        fake_hashed_password = user.password + "asdftest"
        db_user = User(email=user.email, password=fake_hashed_password, information=user.information)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        user = User(**db_user.__dict__)
        return user

    def get_user(self, user_id: int) -> User | None:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        user = User(**db_user.__dict__)
        return user

    def get_user_by_email(self, email: str) -> User | None:
        db_user = self.db.query(User).filter(User.email == email).first()
        if db_user is None:
            return None
        user = User(**db_user.__dict__)
        return user

    def get_user_list(self, skip: int = 0, limit: int = 100) -> list[User] | None:
        db_users = self.db.query(User).offset(skip).limit(limit).all()
        if not db_users:
            return None
        users = [User(**user.__dict__) for user in db_users]
        return users
