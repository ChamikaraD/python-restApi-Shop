
from fastapi import APIRouter, status, HTTPException
from models import UserCreate, UserResponse
from repositories import UserRepository
from services import UserService,UserServiceException

router = APIRouter(prefix="/users")

user_service = UserService(UserRepository())

@router.post("/",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate)->UserResponse:

    try:
        return user_service.create_user(user)
    except UserServiceException as e:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail=str(e))

