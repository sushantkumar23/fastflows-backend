from pydantic import BaseModel


class Response(BaseModel):
    id: str
    user_id: str
    prompt_id: str
    text: str
    is_deleted: bool
    created_at: str


class ResponseBody(BaseModel):
    prompt_id: str
    text: str
