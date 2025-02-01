# from sqlalchemy.ext.asyncio import AsyncSession
#
# from api.v1.views.users import UserCreateSchema
# from core.repositories import UserRepo
#
#
# class UserService:
#     user_repo = UserRepo
#
#     @classmethod
#     async def get_all_users(
#         cls,
#         session: AsyncSession,a
#     ):
#         users = await cls.user_repo.get_all(session=session)
#         return users
#
#     @classmethod
#     async def create_user(
#         cls,
#         session: AsyncSession,
#         user: UserCreateSchema,
#     ):
#         new_user = await cls.user_repo.create(
#             session=session,
#             value=user,
#         )
#         return new_user
