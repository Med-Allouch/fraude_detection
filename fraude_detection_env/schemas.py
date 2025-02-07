from pydantic import BaseModel
from typing import Optional

class ClaimBase(BaseModel):
    id: int
    age: int
    sex: str
    bmi : float
    children : int
    region: str
    charges: str


class ClaimCreate(ClaimBase):
    pass

class Claim(ClaimBase):
    id: int

    class Config:
        orm_mode = True
