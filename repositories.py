from datetime import datetime
from typing import Dict, Optional

from models import UserResponse,UserCreate


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



