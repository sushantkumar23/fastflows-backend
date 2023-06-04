from typing import Any, Dict, List, Optional

import openai
from pydantic import BaseModel

from .oai_models import oai_models


class OAIManager(BaseModel):
    api_key: str

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_key = self.api_key

    def get_chat_completion(
        self,
        *,
        messages: List[Dict[str, str]],
        model: str = "gpt-4",
        params: dict = {},
    ):
        # TODO: add request_timeout param and error handling for it
        # TODO: use async version of ChtCompletion api
        if model not in oai_models:
            raise ValueError(
                f"model {model} not in davinci/gpt OpenAI models: {oai_models}"
            )

        default_params = {
            "temperature": 0.1,
            "max_tokens": 150,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0.6,
            # "stop": ["\n", " Human:", " AI:"],
        }
        params = {**default_params, **params}
        response = openai.ChatCompletion.create(  # response = openai.Completion.create(model=model, prompt=prompt, **params)
            model=model,
            messages=messages,
            **params,
        )

        return {
            # "response": response.choices[0].text, # for completion
            "response": response.choices[0].message.content,  # for chat
            "response_obj": response,
            "model": model,
        }
