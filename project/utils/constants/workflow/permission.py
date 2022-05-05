from enum import auto

from fastapi_utils.enums import StrEnum


class EDocRole(StrEnum):
    INITIALIZER = auto()
    CONTROLLER_BRANCH = auto()
    APPROVER_BRANCH = auto()

    REAPPRAISE_HEADQUARTER = auto()
    CONTROLLER_HEADQUARTER_1 = auto()
    CONTROLLER_HEADQUARTER_2 = auto()
    CONTROLLER_HEADQUARTER_3 = auto()
    APPROVER_HEADQUARTER_1 = auto()
    APPROVER_HEADQUARTER_2 = auto()
    APPROVER_HEADQUARTER_3 = auto()
    APPROVER_HEADQUARTER_4 = auto()
    APPROVER_HEADQUARTER_5 = auto()

    def to_group_role_id(self) -> str:
        return {
            EDocRole.INITIALIZER: "16499863-60ac-42e8-8ec8-d6dba95116a5",
            EDocRole.CONTROLLER_BRANCH: "250e3bed-02f9-4dc9-8771-a7076390e43f",
            EDocRole.APPROVER_BRANCH: "21e482e6-c37c-47f1-81cd-f5bd522241b6",
        }.get(self, "")
