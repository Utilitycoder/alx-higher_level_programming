#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Create engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a new session
    session = Session()

    # Query all State objects from the database and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the states
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
