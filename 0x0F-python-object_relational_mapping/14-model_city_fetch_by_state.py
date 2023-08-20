#!/usr/bin/python3

""" Prints all City objects from the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states = session.query(City, State) \
        .filter(State.id == City.state_id).order_by(City.id).all()

    for city, state in cities_states:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
