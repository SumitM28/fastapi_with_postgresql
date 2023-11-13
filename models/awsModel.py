from sqlalchemy import String, Column, Integer, Float
from database import Base

class Tenant(Base):
    __tablename__ ="tenants"

    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Integer)
    month = Column(String)
    tenantName = Column(String)
    owner = Column(String)
    Department = Column(String)
    costCenter = Column(Integer)
    another_cost = Column(Float)
    Forecasted = Column(String)


class Costs(Base):
    __tablename__ = 'costs'
    id = Column(Integer, primary_key=True, index=True)
    azure = Column(Float)
    gcp = Column(Float)
    aws = Column(Float)