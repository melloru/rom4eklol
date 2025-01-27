from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.models import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    @classmethod
    async def get_user_db(cls, session: "AsyncSession"):
        yield SQLAlchemyUserDatabase(session, User)
