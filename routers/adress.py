from fastapi import APIRouter
from crud.adress import *
from data_base import adress_table
from shemas.adress import Adress

router = APIRouter(prefix="/user")

@router.get("/all")
def get_adress():
    return get_all()


@router.post("/create")
def add_adress(adress: Adress):
    return new_adress(adress)


@router.get("/get_by_city/{city}")
def get_user_by_city(city: str):
    return get_by_city(city)

@router.delete("/delite_users")
def delite_adress_by_city(city: str):
     adress_table.remove(get_by_city(city))


@router.put("/update_last_name/{user_name}")
def update_adress(city: str, adress: Adress):
    return get_by_row_city(city, adress)