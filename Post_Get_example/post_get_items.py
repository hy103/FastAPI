from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Store posted names here (acts like a temp database)
rider_list = []

class NameRequest(BaseModel):
    name: str

# POST request to add a rider
@app.post("/bike_riders")
async def post_rider_details(request: NameRequest):
    rider_list.append(request.name)
    return {"message": f"Hello, {request.name}!"}

# GET request to retrieve all posted riders
@app.get("/bike_riders")
async def get_rider_details():
    return {"riders": rider_list}
