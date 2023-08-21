from models import Uld, Flight, Caster_deck
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///uld_tracker.db")
Session = sessionmaker(binf=engine)
session = Session()

import ipdb; ipdb.set_trace()
from faker import Faker
import random
#working with api and retrieving json data
import requests
import json

#response = requests.get(API_URL)
#json_data = json.loads(response.text)

