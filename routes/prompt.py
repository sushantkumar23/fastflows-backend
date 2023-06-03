import uuid

from fastapi import APIRouter, Depends

from auth import get_current_user
from models.prompt import PromptRequest
from src.prompt import create_prompts, delete_prompts, get_prompts

router = APIRouter(prefix="/prompt", tags=["Prompt APIs"])


@router.get("/", description="Get prompt by id")
def get_prompt(prompt_id: uuid.UUID, user_id=Depends(get_current_user)):
    return get_prompts(prompt_id)


@router.post("/", description="Create a new prompt")
def create_prompt(prompt: PromptRequest, user_id=Depends(get_current_user)):
    return create_prompts(prompt.chart_id, prompt.text, prompt.llm_model, user_id)


@router.delete("/", description="Delete a prompt")
def delete_prompt(prompt_id: uuid.UUID, user_id=Depends(get_current_user)):
    return delete_prompts(prompt_id)
