from src.client import supabase
from fastapi.responses import JSONResponse
import uuid


def get_user_charts(user_id):
    res = (
        supabase.from_("charts")
        .select("id, name, user_id, type, created_at")
        .eq("user_id", user_id)
        .eq("is_deleted", False)
        .execute()
    )
    if len(res.data) == 0:
        return {"message": "No charts found"}
    return {"data": res.data}


def create_chart(chart_name, chart_type, user_id):
    res = (
        supabase.from_("charts")
        .insert({"user_id": user_id, "name": chart_name, "type": chart_type})
        .execute()
    )
    if len(res.data) == 0:
        return JSONResponse(status_code=400, content={"message": "Invalid chart details provided"})
    return {"data": res.data[0]["id"]}


def delete_chart(chart_id: uuid.UUID):
    res = (
        supabase.from_("charts")
        .update({"is_deleted": True})
        .eq("id", chart_id)
        .execute()
    )
    if len(res.data) == 0:
        return {"message": "Invalid chart id"}
    return {"data": res.data[0]["id"]}
