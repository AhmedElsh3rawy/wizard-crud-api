from sqlalchemy import Column, String, Integer
from database import Base


class Wizard(Base):
    __tablename__ = "wizards"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    house = Column(String, index=True, nullable=False)
    gender = Column(String, index=True, nullable=False)
