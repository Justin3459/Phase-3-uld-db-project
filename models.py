from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import faker 

import argparse
Base = declarative_base()

class Uld(Base):
    __tablename__ = "uld"
    id = Column(Integer, primary_key=True)
    uld_name = Column(String)
    status = Column(String)
    caster_id = Column(Integer, ForeignKey("caster_deck.id"))

    def handle_uld_status():

        pass
    def delete_uld():
        pass

         
    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.uld_name} \n"
    

class Flight(Base):
    __tablename__ = "flight"

    id = Column(Integer, primary_key=True)
    flight_name = Column(String)

    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.flight_name} \n"

class Caster_deck(Base):
    __tablename__ = "caster_deck"

    id = Column(Integer, primary_key=True)
    caster_deck = Column(String)
    uld = relationship("Uld", backref="caster_deck")

    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.caster_deck} \n"


if __name__ == "__main__":
    engine = create_engine("sqlite:///uld_tracker.db")
    Base.metadata.create_all(engine)


