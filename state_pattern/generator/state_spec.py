import json
from typing import Dict, List

from pydantic import Field

from transition_spec import TransitionSpec
from project.core import CustomBaseModel
from project.utils import functions


class StateSpec(CustomBaseModel):
    id: str = Field(None)
    name: str = Field(None)
    documentation: Dict = Field(None)
    possible_states: List[TransitionSpec] = Field([])

    @staticmethod
    def process_node_pipeline(name: str) -> str:
        parts = name.split("_")
        if len(parts) >= 2:
            return parts[1].upper()
        return None

    def to_node(self) -> str:
        return json.dumps({
            "product_group_id": "LOAN",
            "process_id": self.process_node_pipeline(self.id),
            "name": self.name,
            "activated_flag": 1,
            "code": self.id,
            "is_start_node": self.documentation.get("is_start_node"),
            "state_group": self.documentation.get("state_group"),
        }, ensure_ascii=False)

    def to_state(self) -> str:
        possible_states_str = ",\n".join(map(lambda t: t.to_possible_state(), self.possible_states))
        roles = self.documentation.get("roles", [])
        write = ", ".join([f"EDocRole.{r}" for r in roles])
        permission_str = f"""PermissionSchema(
            write=[{write}]
        )
        """
        return f"""
class {functions.to_pascal_case(self.id)}(State):
    _state_id = EState.{self.id}

    @property
    def accessible_permissions(self) -> PermissionSchema:
        return {permission_str}

    def next_state(self, action: EAction, path: str) -> 'State':
        next_state = self.possible_states.get(action)
        if not next_state:
            logger.debug(f"action: {chr(123)}action{chr(125)}, path: {chr(123)}path{chr(125)}, action cant move to next state")
            raise LOSException.with_error(loc=["next_state"], code=error_code.CANNOT_CHANGE_STATE, status_code=status.HTTP_412_PRECONDITION_FAILED)

        if not self.compare_path(path, next_state["path"]):
            logger.debug("path not match next state")
            raise LOSException.with_error(loc=["next_state"], code=error_code.CANNOT_CHANGE_STATE, status_code=status.HTTP_412_PRECONDITION_FAILED)

        clazz = self.get_class_from_state_id(next_state["id"])
        ctx = self.ctx
        ctx.set_state(clazz(ctx, pre_transition_id=next_state["transition_id"]))
        return ctx.state

    def _hide_if_done_have_permission(self, possible_state: Dict, permission) -> Dict:
        username_has_write_permission = self.ctx.allocate.get_user_identity_by_role(permission)
        return possible_state if (username_has_write_permission == self.ctx.user.identity) else {chr(123) + chr(125)}
        
    @property
    def possible_states(self) -> Dict:
        write_permission = self.accessible_permissions.write[0]
        return self._hide_if_done_have_permission(
            {chr(123)}
            {possible_states_str}
            {chr(125)},
            write_permission
        )
        """
