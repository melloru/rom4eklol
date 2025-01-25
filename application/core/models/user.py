from datetime import datetime

from sqlalchemy import func, String

from core.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(21),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
