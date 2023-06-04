from llmsdd.core import SDDSchema


class Subgraph(SDDSchema):
    id: str = ""
    label: str = ""
    class_: str = ""

    """
    TODO
    1. Need to add a list of nodes and edges to the subgraph
    2. Need to add an "end" property to the subgraph
    """

    def __repr__(self):
        return f"subgraph {self.id}[{self.label}]:::{self.class_}"

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return f"""{
            'id': {self.id},
            'label': {self.label},
            'class': {self.class_}
        }
        """

    def to_mermaid(self):
        return self.__repr__()
