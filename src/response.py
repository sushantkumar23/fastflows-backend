from src.client import supabase
from fastapi.responses import JSONResponse


def get_responses(response_id):
    res = (
        supabase.from_("responses")
        .select("id, prompt_id, text, created_at")
        .eq("id", response_id)
        .execute()
    )
    if len(res.data) == 0:
        return {"message": "Invalid 'response_id' provided"}
    return {"data": res.data[0]}


def create_responses(prompt_id, response_text, user_id):
    res = (
        supabase.from_("responses")
        .insert(
            {
                "prompt_id": prompt_id,
                "text": response_text,
            }
        )
        .execute()
    )
    if len(res.data) == 0:
        return JSONResponse(
            status_code=400, content={"message": "Invalid response details provided"}
        )
    return {"data": res.data[0]["id"]}


def delete_responses(response_id):
    res = (
        supabase.from_("responses")
        .update({"is_deleted": True})
        .eq("id", response_id)
        .execute()
    )
    if len(res.data) == 0:
        return {"message": "Invalid 'response_id' provided"}
    return {"data": res.data[0]["id"]}
