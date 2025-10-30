from fastapi import FastAPI
from rdkit import Chem

app = FastAPI()

# In-memory storage for demonstration
items = [
    {"id": 1, "smiles": "Cc1ccccc1", "name": "Toluene"},
    {"id": 2, "smiles": "CCO", "name": "ethanol"},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Substructure Search App!"}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items")
def add_item(item: dict):
    item["id"] = len(items) + 1
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    for idx, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            items[idx].update(item)
            return items[idx]
    return {"error": "Item not found"}

@app.put("/items")
def search_item(item: dict):
    output = []
    search = []
    search.update(item)
    search_val = Chem.MolFromSmiles(search["smiles"])
    for _, existing_item in enumerate(items):
        existing_item_val = Chem.MolFromSmiles(existing_item["smiles"])
        match = existing_item_val.HasSubstructMatch(search_val)
        if match:
            output.append(existing_item)
    return output
#Error message should be added

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(items):
        if item["id"] == item_id:
            deleted = items.pop(idx)
            return {"deleted": deleted}
    return {"error": "Item not found"}

