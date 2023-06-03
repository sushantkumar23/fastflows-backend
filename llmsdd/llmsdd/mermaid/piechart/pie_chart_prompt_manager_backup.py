from llmsdd.core import Instructions, Prompt, PromptHistory, PromptManager

from .pie_chart_schema import PieChartSchema


class PieChartPromptManager(PromptManager):
    schema0 = PieChartSchema()
    prompt0 = Prompt(
        schema_in=schema0,
        schema_out=schema0,
        prompt_system="You are a world class expert in creating pie charts using the mermaid library in Python. You're particularly good at translating natural language instructions from users to a json schema that can be used to generate a pie chart.",
        prompt_user="",
        instructions=Instructions(
            instructions_schema=[
                "You will be given a json schema as input (`Input Schema`). This json schema can be translated to a valid input to the mermaid library in Python. This input will generate a pie chart, and we'll refer to it as the `Input Schema`",
                "You will also be given a natural language request from a user. We'll refer to this as your `User Request`.",
                "Your task is to apply the user's natural language request to the json schema.",
                "If the user's natural language request is valid, then you should return a json schema that is the same as the input json schema, except with the user's natural language request applied to it.",
                "If the user's natural language request is invalid, then you should return a the value `none`, and a string describing the error.",
                "You can assume that the user's natural language request will always be valid English.",
                "You can assume that the user's natural language request will always be a valid request for a pie chart.",
                "You can assume that the user's natural language request will always be a valid request for the input json schema.",
                "You can assume that the user's natural language request will always be a valid request for the output json schema.",
                "You can assume that the user's natural language request will always be a valid request for the output json schema, given the input json schema.",
                "Always respond with a json schema.",
            ],
            instructions_response=[
                "Return your response as a json schema.",
                "Your response json schema should have two keys: `processing_error` and `updated_schema`.",
                "The value of `processing_error` should be `none` if there are no errors, and a string describing the error if there is an error in processing the user's natural language request.",
                "The value of `updated_schema` should be `none` if there are errors, and a json schema if there are no errors. This json schema should be the same as the input json schema, except with the user's natural language request applied to it.",
            ],
            instructions_fewshot=[
                # TODO: add an example for showData
                # TODO: and an example of init (i.e. blank input schema)
                "Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}, User Request: 'Make the title of the pie chart 'My Fruit', Output (your response): {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Fruit', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}}",
                "Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}, User Request: 'Add an extra fruit called 'Bananas' with a value of 40', Output (your response): {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30, 'Bananas': 40}}}",
                "Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}, User Request: 'Remove the fruit 'Apples'', Output (your response): {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Oranges': 20, 'Pears': 30}}}",
                "Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}, User Request: 'Change the value of 'Apples' to 20', Output (your response): {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 20, 'Oranges': 20, 'Pears': 30}}}",
                "Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}, User Request: 'Remove the Watermelon fruit', Output (your response): {'processing_error': 'No key called 'Watermelon' found inside 'dataset'', 'updated_schema': 'none'}",
                "Input Schema: {}, User Request: 'Make the title of the pie chart 'My Fruit', Output (your response): {'processing_error': 'none', 'updated_schema': {'showData': false, 'title': 'My Fruit', 'dataset': {}}}",
                "Input Schema: {}, User Request: 'Add an extra fruit called 'Bananas' with a value of 40', Output (your response): {'processing_error': 'none', 'updated_schema': {'showData': false, 'title': '', 'dataset': {'Bananas': 40}}}",
                "Input Schema: {}, User Request: 'Remove the fruit 'Apples'', Output (your response): {'processing_error': 'No key called 'Apples' found inside 'dataset'', 'updated_schema': 'none'}",
                "Input Schema: {}, User Request: 'Change the value of 'Apples' to 20', Output (your response): {'processing_error': 'No key called 'Apples' found inside 'dataset'', 'updated_schema': 'none'}",
            ],
        ),
        response=None,
    )
    history = PromptHistory()
