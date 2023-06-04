from llmsdd.core import SDDSchema
from llmsdd.mermaid.flowchart.types.enums import NodeShape


class Node(SDDSchema):
    # A unique identifier for the node
    id: str

    """
    Label defines the text that is displayed inside the node.
    1. Simple label: example - id[Label]
    2. Markdown support: example - id["Label with **bold**"]
    3. HTML support: example - id["<b>bold</b>"]
    4. Unicode support: example - id["This ❤ Unicode"]
    """
    label: str

    # Shape of the node & can be mapped to flowchart elements
    shape: NodeShape = NodeShape.rectangle

    # Class defines the CSS class of the node. NODE:::class
    class_: str

    def __repr__(self):
        # Process
        if self.shape == NodeShape.rectangle:
            return f"{self.id}[{self.label}]:::{self.class_}"
        # Alternate Process
        elif self.shape == NodeShape.round:
            return f"{self.id}({self.label}):::{self.class_}"
        # Start/End
        elif self.shape == NodeShape.stadium:
            return f"{self.id}([{self.label}]):::{self.class_}"
        # Sub-process
        elif self.shape == NodeShape.subroutine:
            return f"{self.id}[[{self.label}]]:::{self.class_}"
        # Database
        elif self.shape == NodeShape.cylinder:
            return f"{self.id}[({self.label})]:::{self.class_}"
        # On-page connector
        elif self.shape == NodeShape.circle:
            return f"{self.id}(({self.label})):::{self.class_}"
        # Decision
        elif self.shape == NodeShape.rhombus:
            return f"{self.id}{{self.label}}:::{self.class_}"
        # Preparation
        elif self.shape == NodeShape.hexagon:
            return f"{self.id}{{{self.label}}}:::{self.class_}"
        # Input/Output
        elif self.shape == NodeShape.parallelogram:
            return f"{self.id}[/{self.label}/]:::{self.class_}"
        # Manual Operation
        elif self.shape == NodeShape.trapezoid_alt:
            # TODO: Check the additional slash
            return f"{self.id}[\\{self.label}/]:::{self.class_}"
        # TODO: Add more shapes. Refer to the TODO in enums.py

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return f"""{
            'id': {self.id},
            'label': {self.label},
            'shape': {self.shape},
            'class': {self.class_},
        }
        """

    def to_mermaid(self):
        return self.__repr__()
