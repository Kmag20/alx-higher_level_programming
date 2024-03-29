#!/usr/bin/python3
""" Script that prints the first State object
    from the database hbtn_0e)6_usa """

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
