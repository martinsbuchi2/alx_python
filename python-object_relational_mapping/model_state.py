#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """State class inheriting from Base class """
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name =  Column('name', String(128), nullable=False)

if __name__ == "__main__":
    """ to be imported before calling """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)