from crud.apis.request.user import UserCreateDTO
from crud.repository.user import UserRepository
from crud.schema.user import UserSchema


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request: UserCreateDTO) -> UserSchema:
        user_entity = UserSchema(**request.dict())
        user = self.repository.create_user(user_entity)
        return user

    def get_user(self, user_id: int) -> UserSchema:
        return self.repository.get_user(user_id=user_id)

    def get_user_by_email(self, email: str) -> UserSchema:
        return self.repository.get_user_by_email(email=email)

    def get_user_list(self, skip: int, limit: int) -> list[UserSchema]:
        return self.repository.get_user_list(skip=skip, limit=limit)
