from pydantic import BaseModel


class UserCreds(BaseModel):
    email: str
    password: str
