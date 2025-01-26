from core.repositories import BaseRepo
from core.models import User


class UserRepo(BaseRepo[User]):
    def __init__(self):
        super().__init__(model=User)
