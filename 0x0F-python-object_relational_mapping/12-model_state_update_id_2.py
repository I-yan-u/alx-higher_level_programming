#!/usr/bin/python3
"""
    ORM; using sql objects as python objects
    State class
    Base = declarative_base()
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    point = session.query(State).filter(State.id == 2).first()
    if point:
       point.name = "New Mexico"
       session.commit()
    else:
        print("Not found")
