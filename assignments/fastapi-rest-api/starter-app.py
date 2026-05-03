from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Starter FastAPI Items API")

class ItemCreate(BaseModel):
    name: str = Field(..., example="Notebook")
    price: float = Field(..., example=9.99, ge=0)
    in_stock: bool = Field(True, example=True)

class Item(ItemCreate):
    id: int

# In-memory store: id -> Item
_store: Dict[int, Item] = {}
_next_id = 1


@app.get("/items", response_model=list[Item])
def list_items():
    return list(_store.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = _store.get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, **payload.dict())
    _store[_next_id] = item
    _next_id += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    existing = _store.get(item_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    updated = Item(id=item_id, **payload.dict())
    _store[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in _store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del _store[item_id]
    return None
