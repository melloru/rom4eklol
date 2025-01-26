from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.users.schemas import UserCreateSchema
from core.services import UserService
from core.db_helper import db_helper

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
async def get_all_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    users = await UserService.get_all_users(session=session)
    return users


@router.post("/")
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: UserCreateSchema,
):
    created_user = await UserService.create_user(session=session, user=user)
    return created_user