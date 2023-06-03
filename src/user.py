from src.client import supabase


def signup_user(email: str, password: str):
    res = supabase.auth.sign_up({"email": email, "password": password})
    if res.user is None:
        return {"message": "Error signing up"}
    return {
        "data": {
            "id": res.user.id,
            "email": res.user.email,
            "created_at": res.user.created_at,
        }
    }


def login_user(email: str, password: str):
    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if res.user is None:
        return {"message": "Error signing up"}
    return {
        "data": {
            "access_token": res.session.access_token,
            "refresh_token": res.session.refresh_token,
        },
    }
