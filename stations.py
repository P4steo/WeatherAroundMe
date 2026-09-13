from pydantic import BaseModel
from pydantic import Field


class Station(BaseModel):
    station_id: int = Field(alias="no")
    name: str
    lat: float
    long: float
    active: bool
    rain: bool
    water: bool
    flow: bool
    winddir: bool
    windlevel: bool
    temp: bool
    pressure: bool
    humidity: bool
    sun: bool
    turbidity: bool
    dissolvedoxygen: bool
    redox: bool
    ph: bool
    conductivity: bool
    watertemp: bool


class Measurement(BaseModel):
    station_id: int
    timestamp: str
    value: float
    type: str
