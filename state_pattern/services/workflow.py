import json
from typing import Dict

from fastapi import Depends
from pydantic import ValidationError
from starlette import status
from starlette.datastructures import URL

from project.core import LOSException, service, Service, error_code
from project.utils.constants.workflow.permission import EDocRole
from state_pattern.constants.state import EState
from state_pattern.constants.action import EAction
from state_pattern.repositories import DocumentRepository
from state_pattern.schemas.simple_doc import SimpleDoc
from state_pattern.states.base import NextStateRequest, State


@service
class WorkflowService(Service):
    document_repos: DocumentRepository = Depends(DocumentRepository)

    async def state_interpreter(self, los_id: str, url: URL, action: EAction = None, request: NextStateRequest = None, *args, **kwargs) -> str:
        if not request:
            try:
                request = NextStateRequest(action=action, path=url.path)
            except ValidationError as e:
                raise LOSException(detail=e.errors())

        current_state = await self._get_current_state(los_id, request)
        target_state = await current_state.next_state(request)
        target_state_data = {
            "los_id": los_id,
            "state_request": request.dict(),
            "target_state": target_state.dict()
        }
        return json.dumps(target_state_data)

    async def log_state(self, key, new_document: Dict = None):
        data = json.loads(key)
        if not data:
            raise LOSException.with_error(
                code=error_code.WORKFLOW_LOGGER_SERVICE_ERROR,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        # functions.debug(data)
        request = data["state_request"]
        action = request["action"]
        target_state_dict = data["target_state"]

        if new_document:
            ctx = target_state_dict["ctx"]
            target_state_dict["ctx"] = new_document
            target_state_dict["ctx"]["_user"] = ctx["_user"]

        target_state_id = target_state_dict["_state_id"]
        clazz = State.get_class_from_state_id(target_state_id)
        target_state = clazz.from_dict(target_state_dict, SimpleDoc)
        # await self.__log_state(target_state, action, position)
        await self.document_repos.save({"id": target_state.ctx.identity, "state_id": target_state.state_id})

    async def _get_current_state(self, doc_id: int, request: NextStateRequest = None) -> State:
        doc = await self.document_repos.find_by_id(doc_id)
        doc = SimpleDoc(self.request.user, **doc if doc else {})

        if doc.state_id:
            state_id = doc.state_id
        elif not doc.state_id and (request and request.action == EAction.save):
            state_id = EState.s1_a1_start_event
        else:
            raise LOSException.with_error(loc=["path", "id"], code=error_code.ID_NOT_FOUND, id=doc_id)

        clazz = State.get_class_from_state_id(state_id)
        doc.set_state(clazz(doc))
        return doc.state

    async def state_guide(self, doc_id: int) -> Dict:
        current_state = await self._get_current_state(doc_id)
        button_map = {key: {"id": value["id"], "transition_id": value["transition_id"]} for key, value in (await current_state.possible_states()).items()}
        state_guide = {
            "current_state_id": current_state.state_id,
            "guide": button_map,
        }
        return state_guide
