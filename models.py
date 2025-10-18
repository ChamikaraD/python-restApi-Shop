from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name :str
    email:str
    age:int
    role:str

class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id:int
    created_at :str
    updated_at :str