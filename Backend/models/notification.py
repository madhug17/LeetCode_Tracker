from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime
)

from datetime import datetime

from database.db import Base


class Notification(Base):

    __tablename__ = "Notification"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("Users.id")
    )

    title = Column(String)

    message = Column(String)

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )