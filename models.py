from sqlalchemy import (
    create_engine, Column, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///nameage")
base = declarative_base()

# create a class-based model for the "Artist" table
class Person(base):
    __tablename__ = "Person"
    PersonId = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

human = Person(
    name = "Rebas",
    age = 20

)

session.add(human)
session.commit()

humans=session.query(Person)
for humanb in humans:
    print(humanb.name,humanb.age)