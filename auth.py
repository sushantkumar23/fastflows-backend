from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.client import supabase

bearer_scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    if credentials:
        token = credentials.credentials
        # Validate the token with Supabase
        user = supabase.auth.get_user(token)
        if user:
            return user.user.id
        raise HTTPException(status_code=401, detail="Invalid authorization code")
