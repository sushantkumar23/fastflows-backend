from typing import Dict, Optional

from llmsdd.core import Schema


class PieChartSchema(Schema):
    showData: Optional[bool] = None
    title: Optional[str] = ""
    dataset: Optional[Dict[str, float]] = None

    def __repr__(self):
        if self.showData:
            showData = "showData"
        else:
            showData = ""
        if self.title != "":
            title = f"title {self.title}"
        else:
            title = ""
        data = [f'"{k}" : {v}' for k, v in self.dataset.items()]
        return f"pie {showData} {title} {' '.join(data)}"

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return f"""{{
            'showData': {self.showData},
            'title': {self.title},
            'dataset': {self.dataset}
        }}
        """

    def to_mermaid(self):
        return self.__repr__()
