"""
Question: 4: Write a GET /users route that returns all users, with skip and limit query params applied to the DB query.

"""
from typing import List
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

@app.get("/users/", response_model=List[Read_User], status_code=status.HTTP_200_OK)
def get_users(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):

    user = db.query(DBUser).offset(skip).limit(limit).all()
    
    return user