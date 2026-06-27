from time import timezone
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database.db import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class User(Base):
    __tablename__ = "Users"
    #__table_args__ = {
    ##    "extend_existing":True
    #}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False,index = True)
    email = Column(String, unique=True, nullable=False,index = True)
    password = Column(String, nullable=False)
    is_premium = Column(Boolean, default=False)
    leetcode_username = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    is_admin = Column(Boolean,default=False)
    leetcode_ranking = Column(Integer,nullable = True,index = True)
    easy_solved = Column(Integer,default=0)
    medium_solved = Column(Integer,default = 0)
    hard_solved = Column(Integer,default = 0)
    total_solved = Column(Integer,default = 0)
    contest_rating = Column(Integer,nullable=True)
    contest_global_ranking = Column(Integer,nullable=True)
    contest_top_percentage = Column(Integer,nullable=True)
    contest_attended = Column(Integer,default = 0)
    reset_token = Column(String,nullable=True)
    reset_token_expiry = Column(DateTime,nullable=True)
    # Last time LeetCode data was synced
    last_synced = Column(
        DateTime(timezone=True),
        server_default = func.now()
    )
    # Relationship with Problem model
    # One user can have multiple solved problems
    problems = relationship(
        "Problem",
        back_populates="user"
    )
