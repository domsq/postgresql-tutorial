from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Execute instructions from "chinook" DB
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    """Create class-based model for 'Programmer' table"""
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


class FaveCars(base):
    """Create a table for some of Dom's favourite cars"""
    __tablename__ = "FaveCars"
    CarId = Column(Integer, primary_key=True)
    Make = Column(String)
    Model = Column(String)
    Engine = Column(String)
    BHP = Column(String)


# Define a session, instead of direct DB connection
# Create new instance of sessionmaker, then point to the DB
Session = sessionmaker(db)
# Open actual session by calling Session() subclass
session = Session()
# Create DB using declarative_base subclass
base.metadata.create_all(db)

# Create records in "FaveCars" table
am_db9 = FaveCars(
    Make="Aston Martin",
    Model="DB9",
    Engine="5.9L V12",
    BHP="510"
)

porsche_turbo = FaveCars(
    Make="Porsche",
    Model="996 Turbo",
    Engine="3.6L Flat-6 Twin-Turbo",
    BHP="414"
)

ford_mustang = FaveCars(
    Make="Ford",
    Model="Mustang (2016)",
    Engine="5L V8",
    BHP="435"
)

mclaren_senna = FaveCars(
    Make="McLaren",
    Model="Senna",
    Engine="4L V8 Twin-Turbo",
    BHP="789"
)

ferrari_f40 = FaveCars(
    Make="Ferrari",
    Model="F40",
    Engine="2.9L V8 Twin-Turbo",
    BHP="471"
)

merc_sl65 = FaveCars(
    Make="Mercedes-Benz",
    Model="SL65 AMG",
    Engine="6L V12 Twin-Turbo",
    BHP="604"
)

# Add car instances to session
# session.add(am_db9)
# session.add(porsche_turbo)
# session.add(ford_mustang)
# session.add(mclaren_senna)
# session.add(ferrari_f40)
# session.add(merc_sl65)

# Create records on "Programmer" table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Ever Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL Language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft Founder"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# dominic_quail = Programmer(
#     first_name="Dominic",
#     last_name="Quail",
#     gender="M",
#     nationality="South African / Irish",
#     famous_for="Thoughtful and unique design"
# )


# Add instances of programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(dominic_quail)

# Updating single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.nationality = "South African / Irish"

# Commit our session to the DB
# session.commit()

# Updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# Deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
#              first_name=fname, last_name=lname).first()
# # Defensive Programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " +
#           programmer.last_name)
#     confirmation = input("Are you sure you want to" +
#                          " delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# Query the DB to find all programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

# Query the DB to get the car records
cars = session.query(FaveCars)
for car in cars:
    print(
        car.CarId,
        car.Make,
        car.Model,
        car.Engine,
        car.BHP,
        sep=" | "
    )
