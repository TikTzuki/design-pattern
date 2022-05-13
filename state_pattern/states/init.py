from typing import Dict
from loguru import logger
from starlette import status
from state_pattern.states.base import State, NextStateRequest
from project.core import LOSException, error_code
from state_pattern.states.base import PermissionSchema
from project.utils.constants.workflow.permission import EDocRole
from state_pattern.constants.path import EPath
from state_pattern.constants.state import EState
from state_pattern.constants.transition import ETransition
from project.utils.constants.workflow.action import EAction
class Init(State):
    _state_id = EState.init

    @property
    def accessible_permissions(self) -> PermissionSchema:
        return PermissionSchema(
            write=[]
        )
        

    async def next_state(self, request:NextStateRequest) -> 'State':
        next_state = (await self.possible_states()).get(request.action)
        if not next_state:
            raise LOSException.with_error(loc=["next_state"], code=error_code.CANNOT_CHANGE_STATE, status_code=status.HTTP_412_PRECONDITION_FAILED)

        clazz = self.get_class_from_state_id(next_state["id"])
        ctx = self.ctx
        ctx.set_state(clazz(ctx, pre_transition_id=next_state["transition_id"]))
        return ctx.state

    async def possible_states(self, **kwargs) -> Dict:
        write_permission = self.accessible_permissions.write
        guide = {
            EAction.apply_control: { 
"id": EState.controlling, 
"transition_id": ETransition.init_apply_control_controlling, 
"path": EPath.apply_control_path, 
},
EAction.close: { 
"id": EState.closed, 
"transition_id": ETransition.init_close_closed, 
"path": EPath.close_path, 
}
            }
        return await self._filter_pipeline(
            guide,
            [self._permission_filter],
            permissions=write_permission,
            **kwargs
        )
        