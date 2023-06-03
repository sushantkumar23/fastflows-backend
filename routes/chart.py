import uuid

from fastapi import APIRouter, Depends

from auth import get_current_user
from models.chart import ChartRequest
from src.chart import create_chart, delete_chart, get_user_charts

router = APIRouter(prefix="/chart", tags=["Chart APIs"])


@router.get("/", description="Get all charts for a user")
def get_charts(user_id=Depends(get_current_user)):
    return get_user_charts(user_id)


@router.post("/", description="Create a new chart")
def create_charts(chart: ChartRequest, user_id=Depends(get_current_user)):
    return create_chart(chart.name, chart.type, user_id)


@router.delete("/", description="Delete a chart")
def delete_charts(id: uuid.UUID, user_id=Depends(get_current_user)):
    return delete_chart(id)
