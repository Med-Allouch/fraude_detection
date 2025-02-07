from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from dependency import get_db
from models import Claim

# Initialize FastAPI
app = FastAPI()

# Request model to validate extracted data from Colab
class ClaimData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    region: str
    charges: float  # Changed to float for numerical comparison

# Fraud detection logic based on available fields
def detect_fraud(claim: ClaimData) -> bool:
    """
    Basic fraud detection logic:
    - High BMI (> 35) and low charges (< 2000) might indicate inconsistencies.
    - A very high number of children (e.g., > 10) could be flagged.
    - Specific region patterns can also be flagged (e.g., "southwest").
    """
    if claim.bmi > 35 and claim.charges < 2000:
        return True
    if claim.children > 10:
        return True
    if claim.region.lower() == "southwest" and claim.charges > 50000:
        return True
    return False

# API to process claims
@app.post("/process-claim/")
def process_claim(claim_data: ClaimData, db: Session = Depends(get_db)):
    # Detect fraud
    is_fraudulent = detect_fraud(claim_data)

    # Save the claim to the database
    new_claim_data = claim_data.dict()
    new_claim_data["fraudulent"] = is_fraudulent  # Add fraudulent status
    new_claim = Claim(**new_claim_data)
    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)

    return {"message": "Claim processed successfully", "claim_id": new_claim.id, "fraudulent": is_fraudulent}
