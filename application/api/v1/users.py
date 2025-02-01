from fastapi import APIRouter

from .fastapi_users import fastapi_users

from api.schemas.users import UserUpdate, UserRead


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    )
)
