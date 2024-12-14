from data_base import fake_database
from schema import User

def get_all() -> list[User]:
    return fake_database

def new_user(user: User):
    fake_database.append(user)
    return user

def get_by_name(name: str) -> User | None:
    for user in fake_database:
        if user.first_name.lower() == name.lower():
            return user

def get_by_row_name(user_name: str, user: User):
    for row in fake_database:
        if row.first_name.lower() == user_name.lower():
            row.first_name = user.first_name
            row.last_name = user.last_name
            row.age = user.age
            return user