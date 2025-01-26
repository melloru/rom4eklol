from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

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
