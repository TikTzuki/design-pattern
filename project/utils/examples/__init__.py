__all__ = [
    'COLLATERAL_LTV_EXAMPLES',
    'USER_LOGIN',
    'USER_INFO',
    'GLOBAL_CONFIG',
    'LOGIN_REQUEST',
    'CIC_API_POST_EXAMPLE',
    'COLLATERAL_APPRISE_EXAMPLES',
    'CIC_API_GET_EXAMPLE',
    'DOCUMENT_INITIAL_UUID',
    'DOCUMENT_INITIAL_ID',
    'AUTHORIZED_USER',
    'GRAND_ROLE_S1',
    'CREATED_DOCUMENT_LOS_ID',
    'CREATED_DOCUMENT_LOS_UUID'
]

from .document_initializr import DOCUMENT_INITIAL_ID, DOCUMENT_INITIAL_UUID
from .moderation.s1.grand_role import (
    CREATED_DOCUMENT_LOS_ID, CREATED_DOCUMENT_LOS_UUID, GRAND_ROLE_S1
)
from .normal_loan.cic import CIC_API_GET_EXAMPLE, CIC_API_POST_EXAMPLE
from .normal_loan.collateral import COLLATERAL_LTV_EXAMPLES, COLLATERAL_APPRISE_EXAMPLES
from .user import (
    AUTHORIZED_USER, GLOBAL_CONFIG, LOGIN_REQUEST, USER_INFO, USER_LOGIN
)
