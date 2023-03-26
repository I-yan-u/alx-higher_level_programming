#!/usr/bin/python3
"""
    ORM; using sql objects as python objects
    State class
    Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
        State class; inherits Base.
        __tablename__ (string): name of db table.
        id (int): Unique ID (primary key).
        name (str<128>): name of object.

    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)