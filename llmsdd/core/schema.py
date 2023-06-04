from pydantic import BaseModel


class Schema(BaseModel):
    def __repr__(self):
        pass

    def __str__(self):
        pass

    def to_json(self):
        pass
