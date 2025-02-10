from pydantic import BaseModel

class ClaimBase(BaseModel):
    id: int
    age: int
    sex: str
    bmi : float
    children : int
    region: str
    charges: str



