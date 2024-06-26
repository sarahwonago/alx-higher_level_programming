#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the 'hbtn_0e_6_usa' database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_a(username, password, dbname):
    """
    Lists all State objects that contain the letter 'a' from the specified MySQL database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The name of the database.

    Returns:
        List of State objects.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, dbname))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    session.close()

    return states_with_a

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    states_with_a = list_states_with_a(username, password, dbname)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
