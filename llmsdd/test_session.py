import os

from llmsdd.interfaces import OAIManager
from llmsdd.mermaid.piechart import PieChartPromptManager
from llmsdd.tui import Session, SessionApp

pm = PieChartPromptManager(
    interface=OAIManager(api_key=os.getenv("OPENAI_API_KEY")),
)

x = Session(prompt_manager=pm, app=SessionApp(process_fn=pm.iterate))
x.run()
