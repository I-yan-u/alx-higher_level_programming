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

    queue = session.query(State).order_by(State.id).first()
    if queue == None:
        print("Nothing")
    else:
        print("{}: {}".format(queue.id, queue.name))
