#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(argv[1], argv[2], argv[3], pool_pre_ping=True))
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        ins = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
        for data in ins:
                print("{}: {}".format(data.id, data.name))
        session.close()
