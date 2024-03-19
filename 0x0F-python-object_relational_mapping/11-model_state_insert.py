#!/usr/bin/python3
"""Script that adds the State Object 'Louisiana' to the DB"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)

