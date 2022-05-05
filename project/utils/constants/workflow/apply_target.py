from enum import auto

from fastapi_utils.enums import StrEnum


class EApplyTarget(StrEnum):
    REGION = auto()
    "Vùng"
    HEAD_HEADQUARTER = auto()
    "Phòng phê duyệt và thẩm định"
