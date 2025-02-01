import logging
from typing import Optional, TYPE_CHECKING

from fastapi_users import BaseUserManager, IntegerIDMixin

from core.models import User

if TYPE_CHECKING:
    from fastapi import Request

SECRET = "SECRET"


log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has registered.",
            user.id,
        )

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            f"Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )
