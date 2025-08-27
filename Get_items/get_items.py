from fastapi import FastAPI

app = FastAPI()

user_ids = {
    "Harsha" :1,
    "joe" : 2,
    "Sam" : 3
}

@app.get("/get_items/{get_user_id}")
async def get_items(get_user_id):
    return user_ids.get(get_user_id)
