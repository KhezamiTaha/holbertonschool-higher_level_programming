#!/usr/bin/python3
""" Fetch data from joined tables in MySQL database
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    joined_objects = session.query(State, City).join(
            City).order_by(City.id.asc())
    for state, city in joined_objects:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
