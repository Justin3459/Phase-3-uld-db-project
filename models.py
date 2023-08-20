from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationships
import faker 

Base = declarative_base()

class Uld(Base):
    __tablename__ = "uld"
    id = Column("uld_id", Integer, primary_key=True)
    uld_name = Column("uld_name", String)
    location = Column(String, ForeignKey("caster_deck.id"))

    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.uld_name} \n"
    

class Flight(Base):
    __tablename__ = "flight"

    id = Column("flight_id", Integer, primary_key=True)
    flight_name = Column("flight_name", String)

    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.flight_name} \n"

class Caster_deck(Base):
    __tablename__ = "caster_deck"

    id = Column("caster_deck_id", Integer, primary_key=True)
    caster_deck = Column("caster_deck", String)

    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.caster_deck} \n"

if __name__ == "__main__":
    engine = create_engine("sqlite:///uld_tracker.db")
    Base.metadata.create_all(engine)

