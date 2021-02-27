import sqlalchemy
from sqlalchemy import Column, Integer, Float, String
from ...model import Base

class FactorialCalculations(Base):
    __tablename__ = 'factorial_calculations'
    id = Column(Integer, primary_key=True)
    time_spent = Column(String(999))
    result = Column(String(999))