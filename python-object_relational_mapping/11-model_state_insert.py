#!/usr/bin/python3
""" Fetch data from table in database
"""
import sys

from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    first_session = Session()
    Lousiana_state = State(name="Louisiana")
    first_session.add(Lousiana_state)
    objec_ts = first_session.query(State.id).filter(
            State.name == Lousiana_state.name).order_by(State.id.asc()).all()
    if objec_ts:
        for obj in objec_ts:
            print(f"{obj[0]}")
    else:
        print("Not found")
    first_session.commit()
