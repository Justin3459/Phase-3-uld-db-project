from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base
import faker 

Base = declarative_base()

class Uld(Base):
    __tablename__ = "uld"
    id = Column("uld_id", Integer, primary_key=True)
    uld_name = Column("uld_name", String)

