#!/usr/bin/python3
"""
Definition of State class together with Base Class(declative_base)
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Defines the State Class

    Attributes:
        __tablename__ (str): Table name
        id (integer): State id
        name (string): State name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
