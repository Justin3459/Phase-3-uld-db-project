from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from prettycli import red, blue, green
import faker

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

    def __repr__(self):
        return \
            f"\nID: {self.id} \n"+ \
            f"ULD Name: {self.uld_name} \n" + \
            f"Caster Deck: {self.caster_deck_id}\n" + \
            f"Status: {self.status}"

    def handle_name_change(uld_numb, uld_type):
        uld_name = session.query(Uld).filter_by(uld_name = f"amz{uld_numb}{uld_type.lower()}").first()
        if uld_name:
            #needs validator for input
            user_input = input(blue("Enter new ULD number and Type:\n"))
            uld_name.uld_name = f"amz{user_input}"
            print(green(f"Uld name set to amz{user_input}"))
            session.commit()
        else:
            print(red("Type valid ULD"))
        pass
    def handle_caster_change(uld_numb, uld_type):
        uld_caster = session.query(Uld).filter_by(uld_name = f"amz{uld_numb}{uld_type.lower()}").first()
        if uld_caster:
            #needs validator for input
            user_input = input(blue("Enter caster deck number:\n"))
            uld_caster.caster_deck_id = int(user_input)
            print(green(f"Caster deck set to {user_input}"))
            session.commit()
        else:
            print(red("Type valid ULD"))
        
    def handle_uld_status(uld_numb, uld_type):
        uld_status = session.query(Uld).filter_by(uld_name = f"amz{uld_numb}{uld_type.lower()}").first()
        if uld_status:
            #needs validator for input
            user_input = input(blue("Enter Complete or Incomplete:\n"))
            uld_status.status = user_input
            print(green(f"Uld status set to {user_input}"))
            session.commit()
        else:
            print(red("Type valid ULD"))
        pass
    
    def find(uld_numb, uld_type):
        uld_find = session.query(Uld).filter_by(uld_name = f"amz{uld_numb}{uld_type.lower()}").first()
        if uld_find:
            print(green(f"{uld_find}"))
        else:
            print(red(f"Type valid ULD"))
        
    def list_uld():
        return session.query(Uld.uld_name).all()
        
    def delete_uld(uld_numb, uld_type):
        session.query(Uld).filter_by(uld_name=f"amz{uld_numb}{uld_type.lower()}").delete()
        session.commit()
        print(green(f"Deleted: amz{uld_numb}{uld_type.lower()} "))
        

    def add_uld(uld_numb, uld_type):
        #needs to validate that the uld doesnt exist. create a find or create method?
        session.add(Uld(uld_name=f"amz{uld_numb}{uld_type.lower()}", status = "incomplete", caster_deck = None))  
        session.commit()
        print(green(f"Added: amz{uld_numb}{uld_type.lower()} "))

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


