from core.repositories import BaseRepo
from core.models import User


class UserRepo(BaseRepo[User]):
    model = User
