from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request model
class Item(BaseModel):
    name: str
    description: str

# Response model
class ItemResponse(BaseModel):
    result: str

@app.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    # Custom logic
    return {"result": f"Item {item.name} created successfully!"}