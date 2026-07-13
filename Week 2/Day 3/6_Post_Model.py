"""
Question: 6: Add a Post model with a ForeignKey to User. Write a route GET /users/{user_id}/posts that returns all posts for that user.

"""

from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship
from pydantic import BaseModel, ConfigDict

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    posts = relationship("DBPost", back_populates="author", cascade="all, delete-orphan")

class DBPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    author = relationship("DBUser", back_populates="posts")

Base.metadata.create_all(bind=engine)

class PostRead(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}/posts", response_model=List[PostRead], status_code=status.HTTP_200_OK)
def get_user_posts(user_id: int, db: Session = Depends(get_db)):

    user_exists = db.query(DBUser).filter(DBUser.id == user_id).first()

    if not user_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"User with ID{user_id} was not found. "
        )
    
    posts = db.query(DBPost).filter(DBPost.user_id == user_id).all()

    return posts

