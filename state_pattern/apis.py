from fastapi import APIRouter, Depends, Body, Security
from fastapi.security import HTTPBearer
from fastapi_utils.cbv import cbv
from starlette.requests import Request
from starlette.responses import Response

from project.core import DataResponse
from state_pattern.constants.action import EAction
from state_pattern.schemas.simple_doc import SimpleDoc
from state_pattern.services.document import DocumentService
from state_pattern.services.workflow import WorkflowService

router = APIRouter(
    dependencies=[Security(HTTPBearer())]
)


class ETab:
    STAFF = "Nhan vien"
    CONTROLLER = "Kiem soat vien"
    APPROVER = "Nguoi phe duyet"


@cbv(router)
class Apis:
    request: Request
    workflow_service: WorkflowService = Depends(WorkflowService)
    service: DocumentService = Depends(DocumentService)

    @router.post(
        path="/documents",
        tags=[ETab.STAFF]
    )
    async def create(self, document: SimpleDoc = Body(...)):
        state_key = await self.workflow_service.state_interpreter(None, self.request.url, action=EAction.save)
        new_document = await self.service.save(id, document)
        await self.workflow_service.log_state(state_key, new_document.dict())
        return DataResponse(data=new_document.dict())

    @router.post(
        path="/documents/{id}/apply/control",
        tags=[ETab.STAFF]
    )
    async def apply_control(self, id: int):
        state_key = await self.workflow_service.state_interpreter(id, self.request.url, action=EAction.apply_control)
        await self.service.apply_control(id)
        await self.workflow_service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="/documents/{id}/apply/approve",
        tags=[ETab.CONTROLLER]
    )
    async def apply_approve(self, id: int):
        state_key = await self.workflow_service.state_interpreter(id, self.request.url, action=EAction.apply_approve)
        await self.service.apply_approve(id)
        await self.workflow_service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="/documents/{id}/approve",
        tags=[ETab.APPROVER]
    )
    async def approve(self, id: int):
        state_key = await self.workflow_service.state_interpreter(id, self.request.url, action=EAction.approve)
        await self.service.approve(id)
        await self.workflow_service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="/documents/{id}/return/init",
        tags=[ETab.APPROVER]
    )
    async def return_init(self, id: int):
        state_key = await self.workflow_service.state_interpreter(id, self.request.url, action=EAction.return_init)
        await self.service.return_init(id)
        await self.workflow_service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="/documents/{id}/close",
        tags=[ETab.STAFF, ETab.CONTROLLER, ETab.APPROVER]
    )
    async def close(self, id: int):
        state_key = await self.workflow_service.state_interpreter(id, self.request.url, action=EAction.close)
        await self.service.close(id)
        await self.workflow_service.log_state(state_key)
        return Response(status_code=204)

    @router.get(
        path="{id}/guide"
    )
    async def state_guide(self, id: int):
        return await self.workflow_service.state_guide(id)
