#!/usr/bin/python3
"""create states class and base directive
"""

import sqlalchemy
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class City(Base):
    '''class will be mapped to a table
    '''

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="city")
