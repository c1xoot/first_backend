from pydantic import BaseModel


class Adress(BaseModel):
    city_name: str
    district_name: str
    years: int