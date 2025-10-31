from typing import Optional, List

from pydantic import BaseModel, Field, field_validator


class UserBase(BaseModel):
    name :str = Field(...,min_length =2, max_length=50) # field vise validations for models
    email: str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') # add reggex patter
    age:int =Field(...,ge=18 ,le=100)
    role:str

class UserPatch(BaseModel):
    name:Optional[str]= Field(None,min_length =2, max_length=50)
    email:Optional[str] = Field(None, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')  # add reggex patter
    age:Optional[int] = Field(None, ge=18, le=100)
    role: Optional[str] = None


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id:int
    created_at :str
    updated_at :str


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=200)
    description: str = Field(..., min_length=3)
    price: float = Field(..., ge=0)
    in_stock: bool = True
    tags: List[str] = Field(default_factory=list)


    @field_validator('tags')
    def validate_tags(cls, v:List[str]): #writing a custom validation in pydantic
        if len(v) > 10:
            raise ValueError("Maximum tags allowed  is 10")
        return v

    @field_validator('name')
    def validate_name(cls, v:str):
        if 'unwanted' in v:
            raise ValueError('This name is not allowed')
        return v


class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at : str
    updated_at : str
