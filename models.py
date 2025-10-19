from typing import Optional

from pydantic import BaseModel,Field


class UserBase(BaseModel):
    name :str = Field(...,min_length =2, max_length=50) # field vise validations for models
    email: str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') # add reggex patter
    age:int =Field(...,ge=18 ,le=100)
    role:str

class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id:int
    created_at :str
    updated_at :str