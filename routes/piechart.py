import json
import os
import re

from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from llmsdd.core.prompt_manager import PromptManager
from llmsdd.interfaces import OAIManager
from llmsdd.mermaid.piechart import PieChartPrompt, PieChartSchema

# TODO: Check if this is the correct way to integrate the prompt manager
pm = PromptManager(
    schema0=PieChartSchema(),
    prompt0=PieChartPrompt(),
    interface=OAIManager(api_key=os.getenv("OPENAI_API_KEY")),
)

router = APIRouter(prefix="/piechart", tags=["Pie Chart APIs"])


@router.get("/schema", description="Get pie chart schema for input prompt")
def get_schema(prompt: str, user=Depends(get_current_user)):
    res = pm.iterate(
        with_prompt=prompt,
    )
    res = re.sub(r"'", '"', res)
    try:
        res_json = json.loads(res)
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500, detail="Error parsing JSON response from OpenAI"
        )
    if res_json["processing_error"] == "none":
        mermaid_schema = json_to_mermaid(res_json["updated_schema"])
        return {"data": mermaid_schema}
    raise HTTPException(status_code=500, detail="Error processing prompt")


def json_to_mermaid(data: dict) -> str:
    # Start the mermaid code
    mermaid_code = f'pie title {data["title"]}\n'

    # Loop through each key-value pair in the dataset
    for key, value in data["dataset"].items():
        # Add the data to the mermaid code
        mermaid_code += f'    "{key}" : {value}\n'

    return mermaid_code
