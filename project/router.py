from fastapi import APIRouter

from apps.approval import apis as approval_apis
from apps.moderation import apis as moderation_apis
from apps.s1 import apis as s1_apis
from apps.security import apis as security_apis
from apps.user_profile.profile import router as user_profile_apis
from apps.workflow import apis as workflow_apis

router_v2 = APIRouter()
router_v2.include_router(router=s1_apis.router, prefix="/{los_id}")
router_v2.include_router(router=user_profile_apis.router_module, prefix="/users", tags=["[V2] User Profile"])
router_v2.include_router(router=approval_apis.router, prefix="/approval", tags=["[V2] Approval"])
router_v2.include_router(router=security_apis.router, prefix="/account", tags=["[V2] Security"])
router_v2.include_router(router=moderation_apis.router, prefix="/moderation", tags=["[V2] Moderation"])
router_v2.include_router(router=workflow_apis.router, tags=["[V2] Workflow"])
