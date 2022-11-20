from sqlalchemy.orm import Session, lazyload, joinedload

from crud.db.model.users import User
from crud.entity.user import UserEntity


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserEntity) -> UserEntity:
        fake_hashed_password = user.password + "asdftest"
        db_user = User(email=user.email, password=fake_hashed_password, information=user.information)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        user = UserEntity(**db_user.__dict__)
        return user

    def get_user(self, user_id: int) -> UserEntity | None:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return
        user = UserEntity(**db_user.__dict__)
        return user

    def get_user_by_email(self, email: str) -> UserEntity | None:
        db_user = self.db.query(User).filter(User.email == email).first()
        if db_user is None:
            return None
        user = UserEntity(**db_user.__dict__)
        return user

    def get_user_list(self, skip: int = 0, limit: int = 100) -> list[UserEntity]:
        db_users = self.db.query(User).offset(skip).limit(limit).all()
        users = [UserEntity(**user.__dict__) for user in db_users]
        return users
