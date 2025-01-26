from typing import Type, TypeVar, Generic, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Base


T = TypeVar("T", bound=Base)


class BaseRepo(Generic[T]):
    def __init__(
        self,
        model: Type[T],
    ):
        self.model = model

    async def get_all(
        self,
        session: AsyncSession,
    ):
        stmt = select(self.model)
        result = await session.execute(stmt)
        return result.scalars().all()
