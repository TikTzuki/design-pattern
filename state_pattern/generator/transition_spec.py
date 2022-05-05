import json
from typing import Any

from pydantic import Field
from slugify import slugify

from project.core import CustomBaseModel


class TransitionSpec(CustomBaseModel):
    id: str = Field(None)
    start_node_id: str = Field(None)
    next_node_id: str = Field(None)
    status_out_message: str = Field(None)
    status_out: str = Field(None)
    activated_flag: int = Field(1)

    action: str = Field(None)
    uuid: str = Field(None)

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.status_out = slugify(self.status_out_message).replace("-", "_")

    def to_possible_state(self) -> str:
        return (f"EAction.{self.action}: {chr(123)} \n"
                + f"\"id\": EState.{self.next_node_id}, \n"
                + f"\"transition_id\": ETransition.{self.id}, \n"
                + f"\"path\": EPath.{self.action}_path, \n{chr(125)}")

    def to_node_link(self) -> str:
        return json.dumps({
            "position_group_id": "LOAN",
            "start_node_id": self.start_node_id,
            "next_node_id": self.next_node_id,
            "status_out": self.status_out,
            "status_out_message": self.status_out_message,
            "code": self.id,
            "activated_flag": 1
        }, ensure_ascii=False)
