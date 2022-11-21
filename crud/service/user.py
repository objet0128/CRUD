from crud.dto.user import UserCreateDTO
from crud.domain.user import User
from crud.repository.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request: UserCreateDTO) -> User:
        user_entity = User(**request.dict())
        user = self.repository.create_user(user_entity)
        return user

    def get_user(self, user_id: int) -> User:
        return self.repository.get_user(user_id=user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.repository.get_user_by_email(email=email)

    def get_user_list(self, skip: int, limit: int) -> list[User]:
        return self.repository.get_user_list(skip=skip, limit=limit)
