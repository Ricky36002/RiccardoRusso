from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Creazione del database SQLite
engine = create_engine("sqlite:///database.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definizione del modello dati
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# Creazione delle tabelle nel database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency Injection per la sessione del database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schema Pydantic per validare l'input
class ItemCreate(BaseModel):
    name: str
    description: str

# Endpoint per ottenere tutti gli elementi
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# Endpoint per ottenere un elemento specifico
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Endpoint per aggiungere un nuovo elemento
@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    try:
        db.commit()
        db.refresh(new_item)
        return new_item
    except:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error while creating item")

# Endpoint per eliminare un elemento
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}
