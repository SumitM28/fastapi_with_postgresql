from sqlalchemy import  String,Column
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True,index=True)
    username = Column(String, index=True)

