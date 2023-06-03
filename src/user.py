from src.client import supabase


def signup_user(email: str, password: str):
    res = supabase.auth.sign_up({"email": email, "password": password})
    if res.user is None:
        return "Error creating user"
    return "User created successfully"


def login_user(email: str, password: str):
    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if res.user is None:
        return "Error logging in"
    return "User logged in successfully"
