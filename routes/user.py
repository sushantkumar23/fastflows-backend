from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.user import login_user, signup_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/signup", description="Create a new user")
def signup(email: str, password: str):
    message = signup_user(email, password)
    return JSONResponse(content={"message": message})


@router.post("/login", description="Login a user")
def login(email: str, password: str):
    message = login_user(email, password)
    return JSONResponse(content={"message": message})
