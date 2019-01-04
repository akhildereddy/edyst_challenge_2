from sqlalchemy import Column, Integer, String
from database import Base

class CountRequest(Base):
    __tablename__ = 'CountReq'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique = True)
    count = Column(Integer, nullable = True)

    def __init__(self, url=None):
        self.url = url

    def __repr__(self):
        return '<CountRequest %s>' % (self.url)