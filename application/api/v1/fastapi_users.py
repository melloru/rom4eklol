from fastapi_users import FastAPIUsers

from api.dependencies.users import authentication_backend, get_user_manager

from core.models import User


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)
