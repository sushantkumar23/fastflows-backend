from typing import Optional

from textual import events
from textual.app import App, ComposeResult
from textual.containers import Center, Horizontal, Vertical
from textual.widgets import Button, Header, Input, Label, Markdown, TextLog


class SessionApp(App):
    process_fn: Optional[callable] = None

    def __init__(self, process_fn: Optional[callable] = None, **kwargs):
        super().__init__(**kwargs)
        self.process_fn = process_fn
        self.rendered_schema = None
        self.schema = None
        self.api_key_input = None
        self.user_input = None
        self.prompt_log = None

    def __repr__(self):
        return f"SessionApp name: {self.__class__.__name__}"

    def __str__(self):
        return self.__repr__()

    TITLE = "Develop a pie chart using natural language (get output as mermaid spec)"
    CSS = """
    Screen > schema {
        background: green;
        width: 45%;
        height: 45%;
        color: white;
        padding: 2;
        margin: 2;
        border: solid white;
    }

    Screen > prompt_log {
        background: darkblue;
        width: 45%;
        height: 45%;
        color: white;
        padding: 2;
        margin: 2;
        border: solid white;
        border-title-color: green;
        border-title-background: white;
        border-title-style: bold;
    }

    #OPENAI_API_KEY {
        background: darkblue;
        width: 20%;
        height: 0.5%;
        color: white;
        padding: 2;
        margin: 2;
        border: solid white;
    }

    Button {
        margin: 1 2;
    }

    Input {
        margin: 1 2;
    }

    .box {
        border: solid green;
    }
   """

    def compose(self) -> ComposeResult:
        self.rendered_schema = Markdown(
            "No schema generated yet!", id="rendered_schema"
        )
        self.schema = Vertical(
            Markdown("# Pie Chart Schema"),
            self.rendered_schema,
            Markdown("# Marmaid Syntax (generated from schema)"),
            Markdown("No schema generated yet!", id="rendered_mermaid"),
            classes="schema",
        )

        # Open AI API Key
        self.api_key_input = Input(
            placeholder="Put your OPENAI API KEY here",
            id="openai_api_key_input",
            password=True,
        )
        self.api_key_input.focus()

        # User Query
        self.user_input = Input(placeholder="Your query goes here", id="user_input")

        # Prompt Log
        self.prompt_log = TextLog(
            highlight=True,
            markup=True,
            classes="box",
        )

        yield Vertical(
            Header(),
            Horizontal(
                self.schema,
                self.prompt_log,
                classes="displays",
            ),
            Label("OpenAI API Key", id="insert_api_key"),
            self.api_key_input,
            Label("Your Query", id="insert_query"),
            self.user_input,
            Horizontal(
                Center(
                    Button.success("Send", id="send"),
                    Button.warning("Exit", id="exit"),
                ),
            ),
            id="dialog",
        )

    def on_mount(self) -> None:
        self.screen.styles.background = "purple"  # navy
        self.screen.styles.border = ("heavy", "white")
        self.screen.border_title = "llmsdd: pie chart"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit":
            self.exit()
        if event.button.id == "send":
            print(f"self.user_input.value: {self.user_input.value}")
            self.prompt_log.write(f"User input: {self.user_input.value}")
            self.rendered_schema.value = self.process_fn(self.user_input.value)
            print(f"self.rendered_schema.value: {self.rendered_schema.value}")
