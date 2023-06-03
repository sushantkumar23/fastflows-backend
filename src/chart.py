from src.client import supabase


def get_user_charts(user_id):
    res = (
        supabase.from_("charts")
        .select("id, name, type, created_at")
        .eq("user_id", user_id)
        .eq("is_deleted", False)
        .execute()
    )
    return res.data


def create_chart(chart_name, chart_type, user_id):
    res = (
        supabase.from_("charts")
        .insert({"user_id": user_id, "name": chart_name, "type": chart_type})
        .execute()
    )
    return res.data[0]["id"]


def delete_chart(chart_id):
    res = (
        supabase.from_("charts")
        .update({"is_deleted": True})
        .eq("id", chart_id)
        .execute()
    )
    return res.data[0]["id"]
