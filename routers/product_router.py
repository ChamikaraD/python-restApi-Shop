from fastapi import HTTPException

from fastapi import APIRouter

from models import ProductCreate
from services import ProductServiceException

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(product_create: ProductCreate):
    try:
        return
    except ProductServiceException as e:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail=str(e))