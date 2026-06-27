from sqlalchemy import create_engine # this create_engine is basically a bridge for the database man
from sqlalchemy.orm import sessionmaker # Every API request gets its own temporary database worker.
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = "postgresql://postgres:1658@localhost/postgres"
# link for communicating with the database man
# engine is the actual connection bridge between Python and PostgreSQL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)
# SessionLocal creates separate DB sessions/workers for every request
Base = declarative_base()
# Base is the parent class for all database models/tables
def get_db():
    # creating temporary DB session for current request
    db = SessionLocal()
    try:
        # giving DB session to router/services
        yield db
    finally:
        # after request finishes -> close DB connection
        db.close()