from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class Config:
        orm_mode = True


@app.post('/places/')
async def create_place_view(place: Place):
    return place


@app.get("/")
def home():
    return {"message": "Hello world"}


@app.get("/")
def recommend_vc(
    user_stage: str, user_market: str
):
    return {"description": user_stage, "2": user_market}
