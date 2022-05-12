from fastapi import APIRouter, Depends, Query, Body, Path, Security
from fastapi.security import HTTPBearer
from fastapi_utils.cbv import cbv
from starlette.requests import Request
from starlette.responses import Response

from state_pattern.constants.action import EAction
from state_pattern.schemas.simple_doc import SimpleDoc
from state_pattern.services.workflow import WorkflowService

router = APIRouter(
    dependencies=[Security(HTTPBearer())]
)


@cbv(router)
class Apis:
    request: Request
    service: WorkflowService = Depends(WorkflowService)

    @router.post(
        path="/save"
    )
    async def save(self, id: str = Query(None), document: SimpleDoc = Body(...)):
        state_key = await self.service.state_interpreter(id, self.request.url, action=EAction.save)
        new_document = await self.service.save(id, document)
        await self.service.log_state(state_key, new_document.dict())
        return Response(status_code=204)

    @router.post(
        path="/{id}/apply/control"
    )
    async def apply_control(self, id: str):
        state_key = await self.service.state_interpreter(id, self.request.url, action=EAction.save)
        await self.service.apply_control(id)
        await self.service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="{id}/apply/approve"
    )
    async def apply_approve(self, id: str):
        state_key = await self.service.state_interpreter(id, self.request.url, action=EAction.save)
        await self.service.apply_approve(id)
        await self.service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="{id}/approve"
    )
    async def approve(self, id: str):
        state_key = await self.service.state_interpreter(id, self.request.url, action=EAction.save)
        await self.service.approve(id)
        await self.service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="{id}/return/init"
    )
    async def return_init(self, id: str):
        state_key = await self.service.state_interpreter(id, self.request.url, action=EAction.save)
        await self.service.return_init(id)
        await self.service.log_state(state_key)
        return Response(status_code=204)

    @router.post(
        path="{id}/close"
    )
    async def close(self, id: str):
        state_key = await self.service.state_interpreter(id, self.request.url, action=EAction.save)
        await self.service.close(id)
        await self.service.log_state(state_key)
        return Response(status_code=204)
