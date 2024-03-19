#!/usr/bin/python3
"""Script that links all State object from DB hbtn_03_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()

    states = session.query(State).all()
    for newState in states:
        print("{}: {}".format(newState.id, newState.name))
