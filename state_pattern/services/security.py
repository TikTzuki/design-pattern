import typing

from fast_boot.schemas import AbstractUser
from fastapi.security.utils import get_authorization_scheme_param
from starlette.authentication import AuthenticationBackend, AuthenticationError, AuthCredentials
from starlette.requests import HTTPConnection

from project.core import LOSException
from state_pattern.repositories import UserRepository
from state_pattern.schemas.user import User, UnauthenticatedUser


class AuthenticationFilter(AuthenticationBackend):
    user_repos = UserRepository()

    async def authenticate(self, conn: HTTPConnection) -> typing.Tuple[AuthCredentials, typing.Optional[AbstractUser]]:
        unauthentication_res = AuthCredentials(scopes=[]), UnauthenticatedUser()
        if "login" in conn.url.path:
            return unauthentication_res
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return unauthentication_res
        scheme, credentials = get_authorization_scheme_param(authorization)
        if scheme.lower() != "bearer":
            raise AuthenticationError("Invalid authentication credentials")
        if not (authorization and scheme and credentials):
            return unauthentication_res

        return AuthCredentials(scopes=[]), User.parse_obj(await self.user_repos.find_by_id(int(credentials)))
