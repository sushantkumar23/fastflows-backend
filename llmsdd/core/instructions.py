from typing import List

from pydantic import BaseModel


class Instructions(BaseModel):
    instructions_schema: List[str]
    instructions_response: List[str]
    instructions_fewshot: List[str]

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return "\n".join(
            ["\n# Schema Instructions\n"]
            + self.instructions_schema
            + ["\n# Response Instructions\n"]
            + self.instructions_response
            + ["\n# Fewshot Instructions\n"]
            + self.instructions_fewshot
        )

    def add_instruction_fewshot(self, instruction: str):
        self.instructions_fewshot.append(instruction)
        return self

    def add_instruction_response(self, instruction: str):
        self.instructions_response.append(instruction)
        return self

    def add_instruction_schema(self, instruction: str):
        self.instructions_schema.append(instruction)
        return self
