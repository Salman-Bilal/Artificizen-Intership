"""
Question: 1: Set up SQLAlchemy with SQLite. Create a User model with id, name, email, is_active. Run Base.metadata.create_all() to create the table.

"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)


if __name__ == "__main__":
    print("Creating Database Tables......")

    Base.metadata.create_all(bind=engine)

    print("'users' table created inside 'app.db' successfully!")
