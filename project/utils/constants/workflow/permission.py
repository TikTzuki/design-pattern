from enum import auto

from fastapi_utils.enums import StrEnum


class EDocRole(StrEnum):
    CREATE = auto()
    CONTROL = auto()
    APPROVE = auto()
