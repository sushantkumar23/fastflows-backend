from copy import deepcopy
from typing import Dict, List

from pydantic import BaseModel

from .prompt import Prompt


class PromptHistory(BaseModel):
    history: List[Prompt] = []

    class Config:
        arbitrary_types_allowed = True

    def append(self, record: Dict[str, str]):
        self.history.append(record)
        return self

    def __repr__(self):
        return "\n".join([f"{i}:{j}" for i, j in enumerate(self.history)])

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.history)

    def add_prompt(self, prompt: Prompt):
        self.history.append(prompt)
        return self

    @property
    def latest_prompt(self):
        return deepcopy(self.history[-1])
