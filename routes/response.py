import uuid

from fastapi import APIRouter, Depends

from auth import get_current_user
from models.response import ResponseBody
from src.response import create_responses, delete_responses, get_responses

router = APIRouter(prefix="/response", tags=["Response APIs"])


@router.get("/", description="Get response by id")
def get_response(response_id: uuid.UUID, user_id=Depends(get_current_user)):
    return get_responses(response_id)


@router.post("/", description="Create a new response")
def create_response(response: ResponseBody, user_id=Depends(get_current_user)):
    return create_responses(response.prompt_id, response.text, user_id)


@router.delete("/", description="Delete a response")
def delete_response(response_id: uuid.UUID, user_id=Depends(get_current_user)):
    return delete_responses(response_id)
