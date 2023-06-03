from fastapi import HTTPException, status

from src.client import supabase


async def get_current_user():
    session = supabase.auth.get_session()
    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return session.user.id
