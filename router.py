from fastapi import APIRouter

from data_base import fake_database
from schema import User

router = APIRouter(prefix="/user")

@router.get("/all")
def get_users() -> list[User]:
    return fake_database

@router.post("/create")
def add_user(user: User):
    fake_database.append(user)
    return user

@router.get("/get_by_name/{name}")
async def get_user_by_name(name: str):
    for user in fake_database:
        if user.first_name.lower() == name.lower():
            return user

@router.delete("/delite_users")
def delite_user_by_name(name: str):
    for user in fake_database:
        if user.first_name.lower() == name.lower():
            fake_database.remove(user)

@router.put("/update_last_name/{user_name}")
def update_last_name(user_name: str, user: User):
    for row in fake_database:
        if row.first_name.lower() == user_name.lower():
            row.first_name = user.first_name
            row.last_name = user.last_name
            row.age = user.age
            return user