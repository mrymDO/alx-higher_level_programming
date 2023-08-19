#!/usr/bin/python3

""" prints State  object with the name passed as argument """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print('Not found')

    session.close()
