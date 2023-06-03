from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth import get_current_user
from src.chart import create_chart, delete_chart, get_user_charts

router = APIRouter(prefix="/chart", tags=["chart"])


@router.get("/", description="Get all charts for a user")
def get_charts(user_id=Depends(get_current_user)):
    charts = get_user_charts(user_id)
    return JSONResponse(content={"charts": charts})


@router.post("/", description="Create a new chart")
def create_charts(name: str, type: str, user_id=Depends(get_current_user)):
    chart = create_chart(name, type, user_id)
    return JSONResponse(content={"chart": chart})


@router.delete("/", description="Delete a chart")
def delete_charts(id: str, user_id=Depends(get_current_user)):
    chart = delete_chart(id)
    return JSONResponse(content={"chart": chart})
