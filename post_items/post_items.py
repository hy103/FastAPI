from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Request Body schema
class NameRequest(BaseModel):
    name: str

@app.post("/bike_riders")

async def post_rider_details(request : NameRequest):
    return {"message": f"Hello, {request.name}!"}


