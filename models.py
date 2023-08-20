from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationships
import faker 

Base = declarative_base()

class Uld(Base):
    __tablename__ = "uld"
    id = Column("uld_id", Integer, primary_key=True)
    uld_name = Column("uld_name", String)

class Flight(Base):
    id = Column("flight_id", Integer, primary_key=True)
    flight_name = Column("flight_name", String)

class Caster_deck(Base):
    pass

if __name__ == "__main__":
    engine = create_engine("sqlite:///uld_tracker.db")
    Base.metadata.create_all(engine)

