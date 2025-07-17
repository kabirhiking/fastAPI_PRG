from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'hey': "valo"}


@app.get("/items/{item_id}")
def read_item(item_id : int, q: str = None):
    return {"item_id" : item_id, "query": q}

@app.get("/products/")
def list_products(skip: int=0, limit: int=10):
    return {"skip": skip, "limit": limit}
