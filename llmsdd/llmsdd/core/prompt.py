from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .instructions import Instructions
from .schema import Schema


class Prompt(BaseModel):
    schema_in: Optional[Schema] = None
    schema_out: Optional[Schema] = None
    prompt_system: str
    prompt_user: str
    instructions: Instructions
    response: Optional[str] = None
    response_obj: Any = None  # TODO: model OAI response object
    messages: Optional[List[Dict[str, str]]] = []

    @property
    def all_instructions(self):
        return "\n".join(
            [f"* {i}" for i in self.instructions.instructions_schema]
            + [f"* {i}" for i in self.instructions.instructions_response]
            + [
                "\n\nHere are some examples of `Input Schema`, `User Request`, and `Output (your response)`:"
            ]
            + [f"* {i}" for i in self.instructions.instructions_fewshot]
        )

    @property
    def messages(self):
        prompt = f"This is your current `User Request`: {self.prompt_user}. Please update the `Input Schema` as described above and return the response as a json."
        prompt = self.all_instructions + "\n\n" + prompt
        return [
            {"role": "system", "content": self.prompt_system},
            {"role": "user", "content": prompt},
        ]

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        return f"Prompt name: {self.__class__.__name__}\n\nprompt_user:\n{self.prompt_user}"

    def __str__(self):
        return self.__repr__()
