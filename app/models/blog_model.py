from sqlalchemy import String,Integer,Column
from app.database.database import Base

class UserBlog(Base):

    __tablename__ = 'blogs'
    id = Column(Integer,primary_key= True,index= True)
    name = Column(String)
    description = Column(String)

class UserAuth(Base):
    __tablename__ = 'auth'
    id = Column(Integer,primary_key = True,index = True)
    email = Column(String)
    password = Column(String)
