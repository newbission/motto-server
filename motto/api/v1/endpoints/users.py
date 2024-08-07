from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/users")
async def access_users():
    return 'hi'
