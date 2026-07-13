"""
Question: 3: Write a GET /users/{user_id} route that fetches from the DB and returns 404 if not found.

"""

from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel, EmailStr


DataBase_URL = "sqlite:///./app.db"
engine = create_engine(DataBase_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)



Base.metadata.create_all(bind = engine)



class Read_User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool 

    class Config:
        from_attributes = True


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}", response_model=Read_User, status_code=status.HTTP_200_OK)
def get_users(user_id: int, db: Session = Depends(get_db)):

    user = db.query(DBUser).filter(DBUser.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} was not found"
        )
    return user