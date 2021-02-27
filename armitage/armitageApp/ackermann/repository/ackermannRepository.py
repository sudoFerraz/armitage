import sqlalchemy
from sqlalchemy import Column, Integer, Float, String
from ...model import Base

class AckermannCalculations(Base):
    __tablename__ = 'ackermann_calculations'
    id = Column(Integer, primary_key=True)
    time_spent = Column(String(999))
    result = Column(String(999))