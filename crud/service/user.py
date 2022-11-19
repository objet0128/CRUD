from crud.dto.user import UserCreateDTO
from crud.entity.user import UserEntity
from crud.repository.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request: UserCreateDTO) -> UserEntity:
        user_entity = UserEntity(**request.dict())
        user = self.repository.create_user(user_entity)
        return user

    def get_user(self, user_id: int) -> UserEntity:
        return self.repository.get_user(user_id=user_id)

    def get_user_by_email(self, email: str) -> UserEntity:
        return self.repository.get_user_by_email(email=email)

    def get_users(self, skip: int, limit: int) -> list[UserEntity]:
        return self.repository.get_users(skip=skip, limit=limit)
