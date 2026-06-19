from fastapi import FastAPI, HTTPException
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Issue Tracker API",
    description="REST API for managing issues and tickets.",
    version="1.0.0"
) 

app.include_router(issues_router)
app.middleware("http")(timer_middleware)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"])


'''This is a simple FastAPI application that provides CRUD operations for items.


items = {
    1: {"name": "Item 1", "description": "This is item 1"},
    2: {"name": "Item 2", "description": "This is item 2"},
    3: {"name": "Item 3", "description": "This is item 3"},
}


@app.get("/items")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item:
        return item
    return HTTPException(status_code=404, detail="Item not found") 

@app.post("/items")
def create_item(item: dict):
    if item.get("id") in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.get("id")] = {"name": item.get("name"), "description": item.get("description")}
    return items[item.get("id")]


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = {"name": name, "description": description}
    return items[item_id]



'''


