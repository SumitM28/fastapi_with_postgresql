from fastapi import APIRouter, HTTPException,Depends
from pydantic import BaseModel
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import model

class User(BaseModel):
    id:str
    username:str

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]


# creating user route
@router.post('/create')
def create_user(user:User, db:db_dependency):
    create_user = model.User(id=user.id, username= user.username)
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return {
        'success':True,
        'message':'User created successfully'
    }

# getting a specific user
@router.get('/get/{username}')
def get_user(username:str,db:db_dependency):
    user = db.query(model.User).filter(model.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404,detail='User not found')
    return user


# getting all users
@router.get('/get-all')
def get_all_users(db:db_dependency):
    users = db.query(model.User).all()
    return users

# updating all users
@router.put('/update/{username}')
def update_user(username:str, info: User ,db:db_dependency):
    user = db.query(model.User).filter(model.User.username == username ).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in info.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)


# deleting a user
@router.delete('/delete/{username}')
def update_user(username:str, db:db_dependency):
    user = db.query(model.User).filter(model.User.username == username ).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {
        'success':True,
        'message':'user deleted successfully'
    }