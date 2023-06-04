from typing import Optional

from llmsdd.core import SDDSchema


class Edge(SDDSchema):
    # TODO: Check with the team if we need to add a unique identifier for the edge
    # sourceNodeID and targetNodeID are the unique identifiers for the nodes
    sourceNodeID: str
    targetNodeID: str
    # text is an optional label for the edge
    text: Optional[str] = ""

    def __repr__(self):
        if self.text != "":
            return f"{self.sourceNodeID} -->|{self.text}| {self.targetNodeID}"
        else:
            return f"{self.sourceNodeID} --> {self.targetNodeID}"

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return f"""{
            'sourceNodeID': {self.sourceNodeID},
            'targetNodeID': {self.targetNodeID},
            'text': {self.text}
        }
        """

    def to_mermaid(self):
        return self.__repr__()
