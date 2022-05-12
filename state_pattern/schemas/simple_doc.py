from typing import Any

from fast_boot.schemas import AbstractUser
from pydantic import Field
from sqlalchemy.orm import Session

from project.core import CustomBaseModel
from project.utils import functions
from state_pattern.states.base import Context


class DocContent(CustomBaseModel):
    price: int = Field(0)


class SimpleDoc(CustomBaseModel, Context):
    id: int = None
    state_id: str = None
    content: DocContent = Field(DocContent())
    _user: AbstractUser

    def __init__(self, user: AbstractUser = None, **data: Any):
        super().__init__(**data)
        object.__setattr__(self, "_user", user)

    @property
    def user(self) -> AbstractUser:
        return self._user

    @classmethod
    def from_dict(cls, d):
        functions.debug(d)
        d["user"] = d["_user"]
        return cls(**d)

    @property
    def identity(self) -> str:
        return self.id
