from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import User
from repositories.User_repo import UserRepo
from schemas.User_schema import UserSchema,UserUpdateApiKey

router = APIRouter()

# 1. Create User
@router.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    new_user = User(email=user.email, password=user.password)
    created_user = user_repo.add_user(new_user)
    return {"id": created_user.id, "email": created_user.email}

# 2. Get All Users
@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    users = user_repo.get_all_users()
    return users

# 3. Get User by ID
@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user = user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
def update_user(user_id: int, user_Update: UserUpdateApiKey, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user = user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.api_key=user_Update.api_key
    user_repo.update_user(user)
    return user