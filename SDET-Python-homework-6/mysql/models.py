from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalNumberOfRequests(Base):
    __tablename__ = 'total_number_of_requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_count = Column(Integer)


class RequestsPerType(Base):
    __tablename__ = 'requests_per_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(3000))
    requests = Column(Integer)


class MostFrequentRequests(Base):
    __tablename__ = 'frequent_requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(3000))
    count = Column(Integer)


class LargestRequests(Base):
    __tablename__ = 'largest_requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(3000))
    status = Column(Integer)
    size = Column(Integer)
    ip = Column(String(16))


class Users5xx(Base):
    __tablename__ = 'users_5xx'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16))
    count = Column(Integer)
