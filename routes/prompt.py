from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth import get_current_user
from src.prompt import create_prompts, delete_prompts, get_prompts

router = APIRouter(prefix="/prompt", tags=["prompt"])


@router.get("/", description="Get prompt by id")
def get_prompt(prompt_id: str, user_id=Depends(get_current_user)):
    prompt = get_prompts(prompt_id)
    return JSONResponse(content={"prompt": prompt})


@router.post("/", description="Create a new prompt")
def create_prompt(
    chart_id: str, prompt_text: str, llm_model: str, user_id=Depends(get_current_user)
):
    prompt = create_prompts(chart_id, prompt_text, llm_model, user_id)
    return JSONResponse(content={"prompt": prompt})


@router.delete("/", description="Delete a prompt")
def delete_prompt(prompt_id: str, user_id=Depends(get_current_user)):
    prompt = delete_prompts(prompt_id)
    return JSONResponse(content={"prompt": prompt})
