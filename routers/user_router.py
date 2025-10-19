from typing import List

from fastapi import APIRouter, status, HTTPException
from models import UserCreate, UserResponse
from repositories import UserRepository
from services import UserService,UserServiceException

router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService(UserRepository())

@router.post("/",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate)->UserResponse:

    try:
        return user_service.create_user(user)
    except UserServiceException as e:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail=str(e))


@router.get("/{user_id}",response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id:int)-> UserResponse: # using path parameters
    user = user_service.get_user(user_id)

    if not user:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return user

@router.get("/",response_model=List[UserResponse])
def get_all_users():
    return user_service.get_all_users()