from typing import List

from fast_boot.schemas import AbstractUser
from fast_boot.security.access import hierarchical_roles
from fast_boot.security.access.hierarchical_roles import RoleHierarchy
from pydantic import Field

from project.core import CustomBaseModel


class Permission(CustomBaseModel):
    permission_code: str = Field(None)


class Role(CustomBaseModel):
    role_code: str = Field([])
    permissions: List[Permission] = Field([])


class User(AbstractUser):
    username: str = Field(...)
    roles: List[Role]

    def get_branch_code(self) -> str:
        return None

    def get_branch_parent_code(self) -> str:
        return None

    @property
    def role_hierarchy(self) -> RoleHierarchy:
        role_hierarchy = RoleHierarchy()
        role_hierarchy.roles = list(map(lambda role: hierarchical_roles.Role(role.role_code, list(map(lambda p: p.permission_code, role.permissions))), self.roles))
        return role_hierarchy

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        return self.username

    @property
    def identity(self) -> str:
        return self.username


class UnauthenticatedUser(AbstractUser):
    def get_branch_code(self) -> str:
        pass

    def get_branch_parent_code(self) -> str:
        pass

    @property
    def role_hierarchy(self) -> RoleHierarchy:
        return RoleHierarchy()

    @property
    def is_authenticated(self) -> bool:
        return False

    @property
    def display_name(self) -> str:
        return None

    @property
    def identity(self) -> str:
        return None
