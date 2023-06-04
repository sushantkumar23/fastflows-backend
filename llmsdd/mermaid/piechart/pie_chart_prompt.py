from llmsdd.core import Instructions, Prompt

from .pie_chart_schema import PieChartSchema


class PieChartPrompt(Prompt):
    def __init__(self):
        super().__init__(
            schema_in=PieChartSchema(),
            schema_out=PieChartSchema(),
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
                ],
                instructions_response=[
                    "Return your response as a json schema.",
                    "Always respond with a json schema.",
                    "Your response json schema should have two keys: `processing_error` and `updated_schema`.",
                    "The value of `processing_error` should be `none` if there are no errors, and a string describing the error if there is an error in processing the user's natural language request.",
                    "The value of `updated_schema` should be `none` if there are errors, and a json schema if there are no errors. This json schema should be the same as the input json schema, except with the user's natural language request applied to it."
                    "The updated schema should always contain the keys `showData`, `title`, and `dataset`, and their values should be of the same type as the input schema.",
                    "Inside the `dataset` key, the keys should be strings, and the values should always be floats.",
                    "The `showData` key should always be a boolean.",
                    "The `title` key should always be a string.",
                    "The `dataset` key should always be a dictionary.",
                    "The user may request changes in the values of the keys inside `dataset` by expressing their desired change in relative terms instead of absolute terms. For example, the user may ask you to change the value of `Apples` to `20`, or they may ask you to increase the value of `Apples` by `10`.",
                    "The user may request changes in the values of the keys inside `dataset` by expressing their desired change in percentage terms instead of absolute terms. For example, the user may ask you to change the value of `Apples` to `20`, or they may ask you to increase the value of `Apples` by `10%` or `10 percent`, in which case, if the original value of `Apples` was `40`, then the new value of Apples should be set to `44` (not `10` nor `10%` nor `10 percent`).",
                    "When the user requests a percentage change (expressed as `10% increase` or `5 percent decrease`) in the value of a key inside `dataset`, first calculate the absolute change, and then apply the absolute change to the value of the key inside `dataset`.",
                    "Very very important: do not include `Input Schema` or `User Request` in your response. Only include the keys `processing_error` and `updated_schema` in your response.",
                    # "The user may describe their request in a variety of ways. You should be able to handle all of the following cases:",
                    # "1. The user may ask you to change the value of a key inside the `dataset` key. For example, the user may ask you to change the value of `Apples` to `20`.",
                    # "2. The user may ask you to add a new key inside the `dataset` key. For example, the user may ask you to add a new key called `Bananas` with a value of `40`.",
                    # "3. The user may ask you to remove a key inside the `dataset` key. For example, the user may ask you to remove the key `Apples`.",
                    # "4. The user may ask you to change the value of the `title` key. For example, the user may ask you to change the value of `title` to `My Fruit`.",
                    # "5. The user may ask you to change the value of the `showData` key. For example, the user may ask you to change the value of `showData` to `true`.",
                    # "6. The user may ask you to change the value of the `dataset` key. For example, the user may ask you to change the value of `dataset` to `{}`.",
                    # "7. The user may ask you to change the value of the `title` key. For example, the user may ask you to change the value of `title` to `My Fruit`.",
                    # "8. The user may ask you to change the value of the `showData` key. For example, the user may ask you to change the value of `showData` to `true`.",
                ],
                instructions_fewshot=[
                    # TODO: add an example for showData
                    # TODO: and an example of init (i.e. blank input schema)
                    """Example 1:
                        * Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}
                        * User Request: 'Make the title of the pie chart `My Fruit`'
                        * Desired Output: {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Fruit', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}}""",
                    """Example 2:
                        * Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}
                        * User Request: 'Add an extra fruit called `Bananas` with a value of 40' 
                        * Desired Output: {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30, 'Bananas': 40}}}""",
                    """Example 3:
                        * Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}
                        * User Request: 'Remove the fruit `Apples`'
                        * Desired Output: {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Oranges': 20, 'Pears': 30}}}""",
                    """Example 4:
                        * Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}
                        * User Request: 'Change the value of `Apples` to 20'
                        * Desired Output: {'processing_error': 'none', 'updated_schema': {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 20, 'Oranges': 20, 'Pears': 30}}}""",
                    """Example 5:
                        * Input Schema: {'showData': true, 'title': 'My Pie Chart', 'dataset': {'Apples': 10, 'Oranges': 20, 'Pears': 30}}
                        * User Request: 'Remove the Watermelon fruit'
                        * Desired Output: {'processing_error': 'No key called 'Watermelon' found inside 'dataset'', 'updated_schema': 'none'}""",
                    """Example 6:
                        * Input Schema: {}
                        * User Request: 'Make the title of the pie chart My Fruit'
                        * Desired Output: {'processing_error': 'none', 'updated_schema': {'showData': false, 'title': 'My Fruit', 'dataset': {}}}""",
                    """Example 7:
                        * Input Schema: {}
                        * User Request: 'Add an extra fruit called Bananas with a value of 40'
                        * Desired Output: {'processing_error': 'none', 'updated_schema': {'showData': false, 'title': '', 'dataset': {'Bananas': 40}}}""",
                    """Example 8:
                        * Input Schema: {}
                        * User Request: 'Remove the fruit Apples'
                        * Desired Output: {'processing_error': 'No key called `Apples` found inside 'dataset'', 'updated_schema': 'none'}""",
                    """Example 9:
                        * Input Schema: {}
                        * User Request: 'Change the value of Apples to 20'
                        * Desired Output: {'processing_error': 'No key called `Apples` found inside 'dataset'', 'updated_schema': 'none'}""",
                    """Example 10:
                        * Input Schema: {"showData": true, "title": "My Pie Chart", "dataset": {"Asia": 30, "Europe": 20, "Africa": 50}}
                        * User Request: 'Change Asia to 40%'
                        * Desired Output: {"processing_error": "none", "updated_schema": {"showData": true, "title": "My Pie Chart", "dataset": {"Asia": 42, "Europe": 20, "Africa": 50}}}""",
                    """Example 11:
                        * Input Schema: {"showData": true, "title": "My Pie Chart", "dataset": {"Asia": 30, "Europe": 20, "Africa": 50}}
                        * User Request: 'Increase Europe by 20 percent'
                        * Desired Output: {"processing_error": "none", "updated_schema": {"showData": true, "title": "My Pie Chart", "dataset": {"Asia": 30, "Europe": 24, "Africa": 50}}}""",
                    """Example 12:
                        * Input Schema: {"showData": true, "title": "My Pie Chart", "dataset": {"Men": 35, "Women": 25, "Children": 15}}
                        * User Request: 'Change the title to My Family and remove children and add babies with a value of 5'
                        * Desired Output: {"processing_error": "none", "updated_schema": {"showData": true, "title": "My Family", "dataset": {"Men": 35, "Women": 25, "babies": 5}}}""",
                    """Example 13:
                        * Input Schema: {"showData": true, "title": "My Pie Chart", "dataset": {"Men": 35, "Women": 25, "Children": 15}}
                        * User Request: 'Increase men to 40 and decrease women by 10 percent'
                        * Desired Output: {"showData": true, "title": "My Pie Chart", "dataset": {"Men": 40, "Women": 22.5, "Children": 15}}""",
                    """Example 14:
                        * Input Schema: {"showData": true, "title": "View Share", "dataset": {"Naruto": 22, "Pikachu": 56, "SamuraiX": 16}}
                        * User Request: 'Change the title to My Anime and change Pikachu to 52 and add Goku with a value of 5'
                        * Desired Output: {"processing_error": "none", "updated_schema": {"showData": true, "title": "My Anime", "dataset": {"Naruto": 22, "Pikachu": 52, "SamuraiX": 16, "Goku": 5}}}""",
                    """Example 15:
                        * Input Schema: {"showData": true, "title": "View Share", "dataset": {"Naruto": 22, "Pikachu": 56, "SamuraiX": 16}}
                        * User Request: 'Add Death Note with a value of 10 and do not replace the original input schema'
                        * Desired Output: {"processing_error": "none", "updated_schema": {"showData": true, "title": "View Share", "dataset": {"Naruto": 22, "Pikachu": 56, "SamuraiX": 16, "Death Note": 10}}}""",
                    """Example 16:
                        * Input Schema: {"showData": true, "title": "World Population", "dataset": {"Asia": 60, "Europe": 20, "Africa": 20}}
                        * User Request: 'Add North America with a value of 10 and do not replace the original input schema'
                        * Desired Output: {"processing_error": "none", "updated_schema": {"showData": true, "title": "World Population", "dataset": {"Asia": 60, "Europe": 20, "Africa": 20, "North America": 10}}}""",
                ],
            ),
            response=None,
        )
