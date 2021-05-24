import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database
from sqlalchemy_utils.functions.database import database_exists

from mysql.models import Base

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pass@localhost:3306/TEST_SQL"


@pytest.fixture(scope='session')
def mysql():
    if database_exists(SQLALCHEMY_DATABASE_URI):
        drop_database(SQLALCHEMY_DATABASE_URI)
    create_database(SQLALCHEMY_DATABASE_URI)

    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope='session')
def client(mysql):
    session = sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        bind=mysql
    )()
    yield session
    session.close()
