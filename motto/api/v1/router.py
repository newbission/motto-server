from fastapi import APIRouter
router = APIRouter(prefix="/api/v1")

from motto.api.v1.endpoints.users import router as users_router

# 라우터를 FastAPI 애플리케이션에 포함시킵니다.
router.include_router(users_router)