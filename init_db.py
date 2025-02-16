from dependencies import get_db
from model import Base

db = next(get_db())
Base.metadata.create_all(bind=db.bind)
print("Tables created successfully")
