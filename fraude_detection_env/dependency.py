from sqlalchemy.orm import Session
from dataset import SessionLocal

# Dependency to provide database session
def get_db():
    # Create a new database session instance
    # Each request will get its own session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
