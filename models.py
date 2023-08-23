from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import faker
import ipdb 

import argparse
engine = create_engine("sqlite:///uld_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#uld_caster = Table(
    #"uld_caster",
    #Base.metadata,
    #Column("id", Integer, primary_key=True),
    #Column("uld_id", ForeignKey("uld.id")),
    #Column("caster_id", ForeignKey("caster_deck.id")),)

class Uld(Base):
    __tablename__ = "uld"
    id = Column(Integer, primary_key=True)
    uld_name = Column(String)
    status = Column(String)

    caster_deck_id = Column(Integer, ForeignKey("caster_deck.id"))
    caster_deck = relationship("Caster_deck", back_populates="uld_list", foreign_keys=[caster_deck_id])

    #caster_decks = relationship("Caster_deck", secondary=uld_caster)
    #caster_decks = relationship("Caster_deck", secondary=uld_caster, back_populates="ulds")
    
    def handle_uld_status():
        #this just gets a specific uld. needs to change uld_name = input
        uld_status = session.query(Uld).filter_by(uld_name = "amz1234aax").first()
        if uld_status:
            uld_status.status = "complete"
            session.commit()
        pass

    def list_uld():
        return session.query(Uld.uld_name).all()
        
    def delete_uld(input):
        #this gets a specific uld. needs to be changed to input
        session.query(Uld).filter_by(uld_name=f"amz+{input}lay").first()
        session.commit()
        pass      

    def add_uld():
        #this just adds deleted uld. needs changed to take input
        session.add(Uld(uld_name="amz1234lay", status = "incomplete", caster_deck = "1"))
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

    #uld = relationship("Uld", backref="caster_deck")
    #uld_id = Column(Integer, ForeignKey("uld.id"))
    #uld = relationship("Uld", secondary=uld_caster)

    uld_list = relationship("Uld", back_populates="caster_deck", foreign_keys=[Uld.caster_deck_id])

    def __repr__(self):
        return f"ID: {self.id} \n" + f"ULD Name: {self.caster_deck} \n"

#import ipdb; ipdb.set_trace()
if __name__ == "__main__":
    engine = create_engine("sqlite:///uld_tracker.db")
    Base.metadata.create_all(engine)


