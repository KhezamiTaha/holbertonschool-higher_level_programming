#!/usr/bin/python3
""" Fetch data from table in database
"""
import sys

from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True, echo=True)
    Session = sessionmaker(bind=engine)
    first_session = Session()

    objec_t = first_session.query(State).filter(
            State.id == 2).order_by(State.id.asc()).first()
    if objec_t:
        objec_t.name = "New Mexico"
    first_session.commit()
