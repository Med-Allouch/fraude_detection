from sqlalchemy.orm import Session
from models import Claim
from dataset import SessionLocal

def populate_claims_table():
    db: Session = SessionLocal()

    static_claims = [
        {"age": 25, "sex": "male", "bmi": 22.5, "children": 2, "region": "northeast", "charges": 3000.0, "fraudulent": False},
        {"age": 40, "sex": "female", "bmi": 30.0, "children": 3, "region": "southwest", "charges": 8000.0, "fraudulent": False},
        {"age": 35, "sex": "male", "bmi": 28.5, "children": 0, "region": "northwest", "charges": 5000.0, "fraudulent": False},
        {"age": 60, "sex": "female", "bmi": 27.5, "children": 1, "region": "southeast", "charges": 12000.0, "fraudulent": False},
    ]

    for claim in static_claims:
        db.add(Claim(**claim))
    
    db.commit()
    db.close()
    print("Claims table populated with static data!")

if __name__ == "__main__":
    populate_claims_table()
