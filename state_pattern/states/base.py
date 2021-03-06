import abc
import inspect
from itertools import chain
from typing import Dict, Optional, Type, List, Any, TypeVar

from fast_boot.schemas import AbstractUser
from pydantic import Field

from project.core import CustomBaseModel
from project.utils import functions
from state_pattern import states
from state_pattern.constants.action import EAction
from state_pattern.constants.state import EState


class Context(metaclass=abc.ABCMeta):
    _state: 'State'

    @property
    def state(self):
        return self._state

    def set_state(self, state: 'State') -> None:
        object.__setattr__(self, "_state", state)

    @property
    @abc.abstractmethod
    def identity(self):
        ...

    @property
    @abc.abstractmethod
    def user(self) -> AbstractUser:
        ...

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, d):
        ...

    @abc.abstractmethod
    def dict(self):
        ...

    def __str__(self):
        return {self.identity, self.user, }


C = TypeVar("C", bound=Context)


class NextStateRequest(CustomBaseModel):
    action: EAction = Field(None)
    path: str = Field(None)

    def __init__(self, action: EAction, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action = action
        self.path = path


class State(metaclass=abc.ABCMeta):
    _state_id: str

    def __init__(self, ctx: Context, pre_transition_id: str = None):
        self.ctx = ctx
        self.prev_transition_id = pre_transition_id

    @property
    @abc.abstractmethod
    def accessible_permissions(self) -> 'PermissionSchema':
        ...

    async def next_state(self, request: NextStateRequest) -> 'State':
        ...

    @abc.abstractmethod
    async def possible_states(self, **kwargs) -> Dict:
        """Tùy vào điều kiện của hồ sơ mà có thể xử lý để trả về các state khả kiến khác nhau"""
        ...

    @property
    def state_id(self) -> str:
        return self._state_id

    @staticmethod
    def get_class_from_state_id(state_id: Optional['EState']) -> Type['State']:
        rs = set(filter(
            lambda class_tup:
            inspect.isclass(class_tup[1]) and issubclass(class_tup[1], State) and class_tup[1]._state_id == state_id,
            inspect.getmembers(states)
        ))
        clazz_name, clazz = rs.pop()
        return clazz

    async def _permission_filter(self, possible_state: Dict, permissions, **kwargs) -> Dict:
        granted_permissions = set(chain(*[role.permissions for role in self.ctx.user.role_hierarchy.roles]))
        is_granted_permissions = granted_permissions - set(permissions) != granted_permissions
        return possible_state if is_granted_permissions else {}

    async def _approve_official_filter(self, possible_state: Dict, **kwargs) -> Dict:
        if self.ctx.content.price < 0:
            possible_state.pop(EAction.approve, None)
        return possible_state

    async def _filter_pipeline(self, possible_state, filters: List, **kwargs):
        for filter_func in filters:
            print(possible_state)
            possible_state = await filter_func(possible_state, **kwargs)
            functions.debug(f"func filter: {filter_func}, {possible_state}")
        return possible_state

    async def is_satisfied(self) -> bool:
        raise NotImplementedError()

    def dict(self) -> Dict:
        self.ctx.set_state(None)
        return {"_state_id": self._state_id, "ctx": self.ctx.dict(), "pre_transition_id": self.prev_transition_id}

    @classmethod
    def from_dict(cls, d, context_type: Type[C]) -> 'State':
        ctx = context_type.from_dict(d.get("ctx"))
        state = cls(ctx, d.get("pre_transition_id"))
        ctx.set_state(state)
        return state


class PermissionSchema(CustomBaseModel):
    write: List[Any] = Field([])
    read: List[Any] = Field([])
