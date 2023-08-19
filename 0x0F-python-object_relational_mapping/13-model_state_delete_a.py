#!/usr/bin/python3

""" deletes all objects with a name containing 'a' from db """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_a:
        session.delete(state)
    session.commit()
    session.close()
