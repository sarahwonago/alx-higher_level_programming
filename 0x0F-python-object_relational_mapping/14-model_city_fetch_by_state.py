#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    """Main function to fetch and print City objects."""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    
    Session = sessionmaker(engine)
    
    session = Session()
    
    cities = session.query(City).order_by(City.id).all()
    
    for city in cities:
        state_name = session.query(State.name).filter(State.id == city.state_id).first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))
    
    session.close()

if __name__ == "__main__":
    main()
