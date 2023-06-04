from typing import Any, Dict, List, Optional

from loguru import logger
from pydantic import BaseModel

from .prompt import Prompt
from .prompt_history import PromptHistory
from .schema import Schema


class PromptManager(BaseModel):
    schema0: Optional[Schema] = None
    prompt0: Optional[Prompt] = None
    interface: Any = None
    history: PromptHistory = PromptHistory()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history = self.history.append(self.prompt0)

    def __repr__(self):
        repr = f"schema0: {self.schema0.__class__.__name__}\n"
        repr += f"prompt0: {self.prompt0.__class__.__name__}\n"
        repr += f"target_api: {self.target_api}\n"
        repr += f"interface: {self.interface.__class__.__name__}\n"
        repr += f"history: {self.history.__class__.__name__}\n"
        repr += f"history_length: {len(self.history)}\n"
        return repr

    def __str__(self):
        pass

    def validate_json(self, response: Any):
        # TODO: implement
        return response

    def validate_schema(self, response: Any):
        # TODO: implement
        return response

    def iterate(self, with_prompt: str, use_history: bool = False):
        # TODO: handle `use_history`
        new_prompt = self.history.latest_prompt
        new_prompt.prompt_user = with_prompt

        response = self.interface.get_chat_completion(messages=new_prompt.messages)
        response = self.validate_json(response)
        response = self.validate_schema(response)

        # TODO: Update current_schema (by extracting from response)
        updated_schema = response["response"]  # extract schema from response

        new_prompt.response = response["response"]
        new_prompt.response_obj = response["response_obj"]
        self.history.add_prompt(new_prompt)
        return updated_schema
