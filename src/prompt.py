from src.client import supabase


def get_prompts(prompt_id):
    res = supabase.from_("prompts").select("*").eq("id", prompt_id).execute()
    return res.data[0]


def create_prompts(chart_id, prompt_text, llm_model, user_id):
    res = (
        supabase.from_("prompts")
        .select("sequence_no")
        .eq("chart_id", chart_id)
        .order("sequence_no", desc=True)
        .limit(1)
        .execute()
    )
    if len(res.data) > 0:
        sequence_no = res.data[0]["sequence_no"] + 1
    else:
        sequence_no = 1
    res = (
        supabase.from_("prompts")
        .insert(
            {
                "user_id": user_id,
                "chart_id": chart_id,
                "text": prompt_text,
                "sequence_no": sequence_no,
                "llm_model": llm_model,
            }
        )
        .execute()
    )
    return res.data[0]["id"]


def delete_prompts(prompt_id):
    res = (
        supabase.from_("prompts")
        .update({"is_deleted": True})
        .eq("id", prompt_id)
        .execute()
    )
    return res.data[0]["id"]
