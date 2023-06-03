from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth import get_current_user
from src.response import create_responses, delete_responses, get_responses

router = APIRouter(prefix="/response", tags=["response"])


@router.get("/", description="Get response by id")
def get_response(response_id: str, user_id=Depends(get_current_user)):
    response = get_responses(response_id)
    return JSONResponse(content={"response": response})


@router.post("/", description="Create a new response")
def create_response(
    prompt_id: str, response_text: str, user_id=Depends(get_current_user)
):
    response = create_responses(prompt_id, response_text, user_id)
    return JSONResponse(content={"response": response})


@router.delete("/", description="Delete a response")
def delete_response(response_id: str, user_id=Depends(get_current_user)):
    response = delete_responses(response_id)
    return JSONResponse(content={"response": response})
