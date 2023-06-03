from fastapi import APIRouter

from models.auth import UserCreds
from src.user import login_user, signup_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/signup", description="Create a new user")
def signup(user_creds: UserCreds):
    return signup_user(user_creds.email, user_creds.password)


@router.post("/login", description="Login a user")
def login(user_creds: UserCreds):
    return login_user(user_creds.email, user_creds.password)
