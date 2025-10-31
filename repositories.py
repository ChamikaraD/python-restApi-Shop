from dataclasses import replace
from datetime import datetime
from typing import Dict, Optional, List

from models import UserResponse, UserCreate, UserPatch


class UserRepository:

    def __init__(self):
        self.__data: Dict[int, UserResponse] = {}   #__ dekk dmme encapsulate krnn
        self.__count : int = 1

    def create_user(self, user_data :UserCreate) ->UserResponse:
        user_id = self.__count
        new_user = UserResponse(
            id = user_id,
            name = user_data.name,
            email = user_data.email,
            age = user_data.age,
            role = user_data.role,
            created_at = datetime.now().isoformat(),
            updated_at= datetime.now().isoformat()
        )


        self.__data[user_id] = new_user
        self.__count += 1
        return new_user
    def get_user_by_id(self, user_id:int) -> Optional[UserResponse]:
        if user_id in self.__data.keys():
            return self.__data[user_id]
        return None

    def get_user_by_name(self, user_name :str) -> Optional[UserResponse]:

        for user in self.__data.values():
            if user.name == user_name:
                return user
        return None

    def get_user_by_email(self, email :str) -> Optional[UserResponse]:
         for user in self.__data.values():
             if user.email == email:
                 return user
         return None

    def get_all_users(self, limit:int, offset:int )->List[UserResponse]:
        users = list(self.__data.values())
        return users[offset:offset + limit]

    def replace_user(self,user_id:int, user_update) ->UserResponse:

        replace_user = UserResponse(
            id = user_id,
            name = user_update.name,
            email = user_update.email,
            age = user_update.age,
            role = user_update.role,
            created_at = datetime.now().isoformat(),
            updated_at= datetime.now().isoformat()
        )


        self.__data[user_id] = replace_user
        return replace_user

    def patch_user(self, user_id: int, user_patch:UserPatch):

        existing_user: UserResponse = self.__data[user_id]
        update_data = user_patch.model_dump(exclude_unset=True) # converting our pydantic model to a dict

        updated_user = existing_user.model_copy(update= update_data)
        updated_user.updated_at = datetime.now().isoformat()

        self.__data[user_id] = updated_user

        return updated_user




if __name__ == '__main__':
    user_repo = UserRepository()
    user = UserCreate(name="john", email="jhon@gmail.com", age=20, role="admin")
    user_repo.create_user(user)

    user_repo.patch_user(1, UserPatch(name="jack", age=21))




