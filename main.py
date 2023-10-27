from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


class Coordinates(BaseModel):
    longitude: float = Field(ge=-180, le=180)  # долгота
    start_latitude: float = Field(ge=-90, le=90)  # широта


class artificial_satellite(BaseModel):
    number_satellite: int
    name: str = Field(min_length=2, max_length=20)
    start_coordinates: Optional[list[Coordinates]]


AR_artificial_satellite = [
    {"number_satellite": 1, "name": "f_ds", "start_coordinates": [90, 0]},
    {"number_satellite": 2, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 3, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 4, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 5, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 6, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 7, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 8, "name": "f_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 9, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 10, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 11, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 12, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 13, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 14, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 15, "name": "s_ds", "start_coordinates": [0, 0]},
    {"number_satellite": 16, "name": "s_ds", "start_coordinates": [0, 0]},
]


class user_FIO(BaseModel):
    last_name: str = Field(min_length=2, max_length=25)
    name: str = Field(min_length=2, max_length=25)
    surname: str = "none"


class user_data(BaseModel):
    fio: list[user_FIO]
    mail: str = "none"
    order_coordinates: Coordinates


app = FastAPI()


@app.get("/")
def hello():
    return "Hello"
