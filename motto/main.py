from fastapi import FastAPI
from motto.api.v1.router import router as v1_router

app = FastAPI()

# 라우터를 FastAPI 애플리케이션에 포함시킵니다.
app.include_router(v1_router, prefix="/api/v1")
