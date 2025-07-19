
postgres_url = "postgresql://postgres.jnsacfvvvsaecuyydeno:Rjprc2QhfIQGjtfM@aws-0-us-east-2.pooler.supabase.com:6543/postgres"

from sqlmodel import SQLModel, Field
from typing import Optional

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False
    
from sqlmodel import create_engine, Session

engine = create_engine(postgres_url, echo=True)

from fastapi import FastAPI
from contextlib import asynccontextmanager

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run sync function in a thread (because create_all is sync)
    import anyio
    await anyio.to_thread.run_sync(create_db_and_tables)
    yield

app = FastAPI(lifespan=lifespan)


# POST /items/
@app.post("/items/")
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
from typing import List
from sqlmodel import select

# GET /items/
@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items