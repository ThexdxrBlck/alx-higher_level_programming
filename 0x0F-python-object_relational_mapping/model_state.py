#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    Clasee with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Colum(integer, unique=True, nullable=False, primary_key=True)
    name = Colum(String(128), nullable=False)
