from pydantic import BaseModel


class Chart(BaseModel):
    id: str
    name: str
    type: str
    user_id: str
    is_deleted: bool
    created_at: str


class ChartRequest(BaseModel):
    name: str
    type: str
