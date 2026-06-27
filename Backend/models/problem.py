from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.db import Base
class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    topic = Column(String)
    time_spend = Column(Integer)
    notes = Column(String)
    solved_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    user_id = Column(
        Integer,
        ForeignKey("Users.id")
    )
    user = relationship(
        "User",
        back_populates="problems"
    )