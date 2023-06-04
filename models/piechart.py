from pydantic import BaseModel


class PieChartPromptRequest(BaseModel):
    prompt: str
    latest_schema: str
