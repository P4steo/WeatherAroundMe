import requests
from fastapi import FastAPI
from stations import Station
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("USER_API_KEY")

BASE_URL = "https://pomiary.gdanskiewody.pl/rest"

def fetch_stations():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    r = requests.get(f"{BASE_URL}/stations", headers=headers)
    r.raise_for_status()
    return r.json()["data"]

def fetch_measurement(station_id: int):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    r = requests.get(
        f"{BASE_URL}/measurements/{station_id}/rain/2026-09-12",
        headers=headers
    )
    r.raise_for_status()
    return r.json()["data"]

app = FastAPI()

@app.get("/stations", response_model=list[Station])
def get_stations():
    return fetch_stations()

@app.get("/stations/filter", response_model=list[Station])
def filter_stations(
    name: str | None = None,
    active: bool | None = None
):
    stations = fetch_stations()

    if name:
        stations = [s for s in stations if name.lower() in s["name"].lower()]

    if active is not None:
        stations = [s for s in stations if s["active"] == active]

    return stations

@app.get("/stations/{station_id}", response_model=Station)
def get_station(station_id: int):
    stations = fetch_stations()
    for s in stations:
        if s["no"] == station_id:
            return s
    return {"error": "Station not found"}

@app.get("/stations/{station_id}/measurements")
def get_measurements(station_id: int):
    return fetch_measurement(station_id)
