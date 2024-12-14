from pydantic import BaseModel


class Adress(BaseModel):
    city: str
    district: str