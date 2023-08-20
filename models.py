from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base
import faker 

Base = declarative_base()

class Uld(Base):

