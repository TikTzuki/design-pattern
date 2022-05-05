from enum import Enum

from project.utils.constants.utils import LOAN_TYPE_NORMAL, LOAN_TYPE_CARD


class ETemplateType(str, Enum):
    OLD_NORMAL_LOAN_TEMPLATE = f"OLD_{LOAN_TYPE_NORMAL}"
    NORMAL_LOAN = LOAN_TYPE_NORMAL
    CARD_LOAN = LOAN_TYPE_CARD
