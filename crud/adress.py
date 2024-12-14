from data_base import adress_table
from shemas.adress import Adress

def get_all() -> list[Adress]:
    return adress_table

def new_adress(adress: Adress):
    adress_table.append(adress)
    return adress

def get_by_city(city: str) -> Adress | None:
    for adress in adress_table:
        if adress.city_name.lower() == city.lower():
            return adress

def get_by_row_city(city: str, adress: Adress):
    for row in adress_table:
        if row.city_name.lower() == city.lower():
            row.city_name = adress.first_name
            row.district_name = adress.district_name
            return adress