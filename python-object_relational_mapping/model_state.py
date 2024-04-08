#!/usr/bin/python3
"""create states class and base directive
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''class will be mapped to a table
    '''

    __tablename__ = "states"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

    # city = relationship("City", back_populates="state")
