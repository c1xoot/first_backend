import data_base
from shemas.user import User


def get_all() -> list[User]:
    return data_base.user_table


def new_user(user: User):
    data_base.user_table.append(user)
    return user


def get_by_name(name: str) -> User | None:
    for user in data_base.user_table:
        if user.first_name.lower() == name.lower():
            return user


def get_by_row_name(user_name: str, user: User):
    for row in data_base.user_table:
        if row.first_name.lower() == user_name.lower():
            row.first_name = user.first_name
            row.last_name = user.last_name
            row.age = user.age
            return user
