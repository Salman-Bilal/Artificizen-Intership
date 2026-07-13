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


class Create_User(BaseModel):
    name: str
    email: EmailStr

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

@app.post("/users/", response_model=Read_User, status_code=status.HTTP_201_CREATED)
def usercreate(user_in: Create_User, db: Session = Depends(get_db)):
    exiting_user = db.query(DBUser).filter(DBUser.email == user_in.email).first()
    if exiting_user:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered."
        )
    
    new_db_user = DBUser(
        name = user_in.name,
        email = user_in.email
    )

    db.add(new_db_user)
    db.commit()

    db.refresh(new_db_user)

    return new_db_user
    