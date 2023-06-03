import os
from llmsdd.interfaces import OAIManager
from llmsdd.core.prompt_manager import PromptManager
from llmsdd.mermaid.piechart import PieChartSchema, PieChartPrompt


pm = PromptManager(
    schema0=PieChartSchema(),
    prompt0=PieChartPrompt(),
    interface=OAIManager(api_key=os.getenv("OPENAI_API_KEY")),
)

r1 = pm.iterate(
    with_prompt="Give me a pie chart of the following data: Human: 10%, Orc: 20%, Elf: 30%, Dwarf: 40%"
)
print(r1)
