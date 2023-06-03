from typing import Optional

from loguru import logger
from pydantic import BaseModel

from llmsdd.core.prompt_manager import PromptManager

from .session_app import SessionApp


class Session(BaseModel):
    prompt_manager: Optional[PromptManager]
    app: Optional[SessionApp]

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        return f"Session(prompt={self.prompt}, app={self.app})"

    def __str__(self):
        pass

    def run(self, process_fn: Optional[callable] = None):
        logger.info("Running Session")
        # TODO: run loop: Take a new Prompt, iterate(), and display updated Prompt+Error
        # TODO: if `exit` is chosen, display final Prompt, serialize, and exit
        self.app.run()
        pass
