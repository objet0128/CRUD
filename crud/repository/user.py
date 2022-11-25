from sqlalchemy.orm import Session

from crud.db.model.user import User
from crud.schema.user import UserSchema


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserSchema) -> UserSchema:
        fake_hashed_password = user.password + "asdftest"
        db_user = User(email=user.email, password=fake_hashed_password, information=user.information)  # type: ignore
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        user = UserSchema(**db_user.__dict__)
        return user

    def get_user(self, user_id: int) -> UserSchema | None:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        user = UserSchema(**db_user.__dict__)
        return user

    def get_user_by_email(self, email: str) -> UserSchema | None:
        db_user = self.db.query(User).filter(User.email == email).first()
        if db_user is None:
            return None
        user = UserSchema(**db_user.__dict__)
        return user

    def get_user_list(self, skip: int = 0, limit: int = 100) -> list[UserSchema] | None:
        db_users = self.db.query(User).offset(skip).limit(limit).all()
        if not db_users:
            return None
        users = [UserSchema(**user.__dict__) for user in db_users]
        return users
