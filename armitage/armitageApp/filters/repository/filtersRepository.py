import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, Bool
from ..model import base

class Filters(Base):
    __tablename__ = 'filters'
    id = Column(Integer, primary_key=True)
    words = Column(String(999))
    active = Column(Bool)