from models import Uld, Flight, Caster_deck, uld_caster
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///uld_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

from faker import Faker
import random
#working with api and retrieving json data
#import requests
#import json

fake = Faker()
#response = requests.get(API_URL)
#json_data = json.loads(response.text)

all = Flight,Uld,Caster_deck
session.query(Flight).delete()
#session.commit()
session.query(Uld).delete()
#session.commit()
session.query(Caster_deck).delete()
#session.commit()

ont_data = [
    Uld(uld_name="amz1234dqf", status="incomplete"),
    Uld(uld_name="amz1234lay", status="incomplete"),
    Uld(uld_name="amz1234aax", status="incomplete"),
    Flight(flight_name = "ONT"),
    ]

msp_data =  [
    Uld(uld_name="amz2222dqf", status="incomplete"),
    Uld(uld_name="amz2222aax", status="incomplete"),
    Uld(uld_name="amz2222lay", status="incomplete"),
    Flight(flight_name = "MSP"),
    ]

abe_data =  [
    Uld(uld_name="amz1111dqf", status="incomplete"),
    Uld(uld_name="amz1111aax", status="incomplete"),
    Uld(uld_name="amz1111lay", status="incomplete"),
    Flight(flight_name = "ABE"),
    ]

caster_deck = Caster_deck(caster_deck = "1")
uld = [ 
    Uld(uld_name="amz1234dqf", status="incomplete"),
    Uld(uld_name="amz1234lay", status="incomplete"),
    Uld(uld_name="amz1234aax", status="incomplete"),
    Uld(uld_name="amz2222dqf", status="incomplete"),
    Uld(uld_name="amz2222aax", status="incomplete"),
    Uld(uld_name="amz2222lay", status="incomplete"),
    Uld(uld_name="amz1111dqf", status="incomplete"),
    Uld(uld_name="amz1111aax", status="incomplete"),
    Uld(uld_name="amz1111lay", status="incomplete"),]

all_data = [caster_deck,uld]
session.add_all(uld)
session.add_all([Caster_deck(caster_deck="3")])
#for data in all_data:
    #session.add_all(data)
    #session.commit()
#session.add_all(msp_data)
#session.add_all(abe_data)
#session.add_all(ont_data) 
session.commit()

print("Seeding Done")
import ipdb; ipdb.set_trace()
#for _ in range():
    #create 3 ulds in format of amz(4num)(uld type)