import json
import os
import re

from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from llmsdd.core.prompt_manager import PromptManager
from llmsdd.interfaces import OAIManager
from llmsdd.mermaid.piechart import PieChartPrompt, PieChartSchema
from models.piechart import PieChartPromptRequest

router = APIRouter(prefix="/piechart", tags=["Pie Chart APIs"])


@router.post("/schema", description="Get pie chart schema for input prompt")
def get_schema(prompt: PieChartPromptRequest, user=Depends(get_current_user)):
    if prompt.latest_schema == "":
        pm = PromptManager(
            schema0=PieChartSchema(),
            prompt0=PieChartPrompt(),
            interface=OAIManager(api_key=os.getenv("OPENAI_API_KEY")),
            prompt_template="piechart",
        )
    else:
        prompt.latest_schema = prompt.latest_schema.replace("'", '"')
        prompt.latest_schema = prompt.latest_schema.replace("\n", "")
        prompt.latest_schema = prompt.latest_schema.replace("True", "true")
        prompt.latest_schema = prompt.latest_schema.replace("False", "false")
        latest_schema = PieChartSchema.parse_raw(prompt.latest_schema)
        latest_prompt = PieChartPrompt()
        latest_prompt.schema_in = latest_schema
        pm = PromptManager(
            schema0=latest_schema,
            prompt0=latest_prompt,
            interface=OAIManager(api_key=os.getenv("OPENAI_API_KEY")),
        )
    res = pm.iterate(
        with_prompt=prompt.prompt,
    )
    res = re.sub(r"'", '"', res)
    try:
        res_json = json.loads(res)
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500, detail="Error parsing JSON response from OpenAI"
        )
    if res_json["processing_error"] == "none":
        res_schema = res_json["updated_schema"]
        mermaid_schema = json_to_mermaid(res_schema)
        mermaid_json = PieChartSchema(**res_schema).to_json()
        return {"data": {"schema": mermaid_schema, "json": mermaid_json}}
    raise HTTPException(status_code=500, detail="Error processing prompt")


def json_to_mermaid(data: dict) -> str:
    # Start the mermaid code
    mermaid_code = f'pie title {data["title"]}\n'

    # Loop through each key-value pair in the dataset
    for key, value in data["dataset"].items():
        # Add the data to the mermaid code
        mermaid_code += f'    "{key}" : {value}\n'

    return mermaid_code


def str_to_dict(s):
    return json.loads(s.replace("'", '"'))
