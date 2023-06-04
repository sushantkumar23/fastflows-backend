from typing import List, Optional

from llmsdd.core import SDDSchema
from llmsdd.mermaid.flowchart.types.enums import Orientation


class FlowChartSchema(SDDSchema):
    orientation: Orientation = Orientation.TD
    title: Optional[str] = ""
    # dataset is a list of nodes, edges, and subgraphs
    dataset: List = []

    def __repr__(self):
        if self.title != "":
            title = """
            ---
            title: {self.title}
            ---
            """
        else:
            title = ""
        dataset = "\n".join([str(item) for item in self.dataset])
        return f"{title} flowchart {self.orientation.value}\n{dataset}\n"

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return f"""{
            'orientation': {self.orientation.value},
            'title': {self.title},
            'dataset': {self.dataset}
        }
        """

    def to_mermaid(self):
        return self.__repr__()
