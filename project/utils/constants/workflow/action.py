from enum import auto
from fastapi_utils.enums import StrEnum


class EAction(StrEnum):
    accept_official = auto()

    accept_unofficial = auto()

    apply = auto()

    apply_approve = auto()

    apply_control = auto()

    apply_headquarter_official = auto()

    apply_headquarter_unofficial = auto()

    approve = auto()

    close = auto()

    complaint = auto()

    confirm = auto()

    deny_official = auto()

    deny_unofficial = auto()

    freeze = auto()

    modify_credit_info = auto()

    modify_notification = auto()

    reject = auto()

    return_init = auto()

    return_pre_control = auto()

    save = auto()
