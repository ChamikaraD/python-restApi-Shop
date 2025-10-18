from typing import Optional

from models import UserCreate, UserResponse
from repositories import UserRepository


class UserServiceException(Exception):
    pass
class UserService:

    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data:UserCreate) -> UserResponse:

        if self.user_repository.get_user_by_name(user_data.name) is not None:
            raise UserServiceException ("User name already exists")

        if self.user_repository.get_user_by_email(user_data.email) is not None:
            raise UserServiceException ("Email already exists")

        return self.user_repository.create_user(user_data)

    def get_user(self, id:int)-> Optional[UserResponse]:

        return self.user_repository.get_user_by_id(id)

