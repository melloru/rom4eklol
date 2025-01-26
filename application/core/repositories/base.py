from typing import Type, TypeVar, Generic, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Base


T = TypeVar("T", bound=Base)


class BaseRepo(Generic[T]):
    model: Type[T]

    @classmethod
    async def get_all(
        cls,
        session: AsyncSession,
    ) -> Sequence[T]:
        stmt = select(cls.model)
        result = await session.execute(stmt)
        return result.scalars().all()
