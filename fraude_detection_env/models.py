from sqlalchemy import Boolean, Column, Integer, String, Float
from dataset import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    sex = Column(String, nullable=False)
    bmi = Column(Float, nullable=False)
    children = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
    charges = Column(Float, nullable=False)
    fraudulent = Column(Boolean, nullable=False)

