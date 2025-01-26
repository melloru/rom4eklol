from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from core.models import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
