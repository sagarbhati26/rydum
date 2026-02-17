from fastapi import APIRouter
from app.api.v1.endpoints import beats

api_router = APIRouter()
api_router.include_router(beats.router, prefix="/beats", tags=["beats"])
