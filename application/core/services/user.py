from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories import UserRepo


class UserService:
    user_repo = UserRepo

    @classmethod
    async def get_all_users(
        cls,
        session: AsyncSession,
    ):
        users = await cls.user_repo.get_all(session=session)
        return users
