from fastapi import APIRouter
from crud import *
from data_base import user_table
from schema import User

router = APIRouter(prefix="/user")

@router.get("/all")
def get_users():
    return get_all()


@router.post("/create")
def add_user(user: User):
    return new_user(user)


@router.get("/get_by_name/{name}")
def get_user_by_name(name: str):
    return get_by_name(name)

@router.delete("/delite_users")
def delite_user_by_name(name: str):
     user_table.remove(get_by_name(name))


@router.put("/update_last_name/{user_name}")
def update_last_name(user_name: str, user: User):
    return get_by_row_name(user_name, user)