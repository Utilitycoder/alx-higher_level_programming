#!/usr/bin/env python3
"""
This script lists all State objects that contain the letter "a" from the
database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {} username password database'.format(sys.argv[0]))
        exit(1)

    # Create a connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for all State objects that contain the letter "a"
    states = session.query(State).filter(State.name.like('%a%')).order_by(
        State.id)

    # Display the results
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    # Close the session
    session.close()
