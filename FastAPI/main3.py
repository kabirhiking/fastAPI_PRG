from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from fastapi import FastAPI
from contextlib import asynccontextmanager

# DB model
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False

# Request model (no id)
class ItemCreate(SQLModel):
    name: str
    price: float
    is_offer: bool = False

# DB engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# FastAPI app
app = FastAPI(lifespan=lifespan)

# POST /items/
@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate):
    db_item = Item.from_orm(item)
    with Session(engine) as session:
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

# GET /items/
@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
