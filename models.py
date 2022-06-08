from sqlalchemy import (
    create_engine, Column, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///nameage")
base = declarative_base()

def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name
# create a class-based model for the "Artist" table
class Person(base):
    __tablename__ = "Person"
    PersonId = Column(Integer, primary_key=True)
    name = Column(String(25))
    age = Column(Integer)


def __repr__(self):
    return f"{self.PersonId} Name: {self.name} Age:{self.age}"

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