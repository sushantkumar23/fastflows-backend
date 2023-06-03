from pydantic import BaseModel


class Prompt(BaseModel):
    id: str
    user_id: str
    chart_id: str
    sequence_no: int
    text: str
    llm_model: str
    is_deleted: bool
    created_at: str


class PromptRequest(BaseModel):
    chart_id: str
    text: str
    llm_model: str
