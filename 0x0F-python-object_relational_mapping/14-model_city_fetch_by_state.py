#!/usr/bin/python3
"""
script that prints all City objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City):
        for state in session.query(State).filter(State.id == city.state_id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
