from fastapi import FastAPI, Depends
from dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from model import Wizard
from pydantic import BaseModel

app = FastAPI()


class WizardCreate(BaseModel):
    name: str
    house: str
    gender: str


@app.get("/")
def read_root():
    return "Hello, World!"


@app.get("/db-health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # Runs a simple test query
        return {"status": "Database Connected"}
    except Exception as e:
        return {"status": "Database NOT Connected", "error": str(e)}


@app.post("/wizards/")
def create_wizard(wizard: WizardCreate, db: Session = Depends(get_db)):
    new_wizard = Wizard(
        name=wizard.name, house=wizard.house, gender=wizard.gender)
    db.add(new_wizard)
    db.commit()
    db.refresh(new_wizard)
    return new_wizard
