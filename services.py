from typing import Optional

from models import UserCreate, UserResponse, UserUpdate, UserPatch
from repositories import UserRepository


class UserServiceException(Exception):
    pass

class ProductServiceException(Exception):
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

    def get_all_users(self,limit:int=10, offset:int=0):
        return self.user_repository.get_all_users(limit, offset)

    def replace_user(self,user_id:int, user_update: UserUpdate) -> UserResponse:

        if self.user_repository.get_user_by_name(user_id.name) is not None:
            raise UserServiceException("User name already exists")

        if self.user_repository.get_user_by_email(user_id.email) is not None:
            raise UserServiceException("Email already exists")

        return self.user_repository.replace_user(user_id, user_update)

    def patch_user(self, user_id:int, user_patch: UserPatch)-> UserResponse:

        if self.user_repository.get_user_by_name(user_id) is not None:
            raise UserServiceException("User name already exists")

        if self.user_repository.get_user_by_name(user_patch.name) is not None:
            raise UserServiceException("User name already exists")

        if self.user_repository.get_user_by_email(user_patch.email) is not None:
            raise UserServiceException("Email already exists")

        return self.user_repository.patch_user(user_id, user_patch)

