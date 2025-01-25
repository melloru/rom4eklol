from datetime import datetime

from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(21),
        nullable=False,
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
