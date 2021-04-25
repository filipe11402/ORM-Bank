from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Account(Base):
    __tablename__ = 'Accounts'

    id = Column(Integer, Sequence('account_id_seq'), primary_key=True)
    firstname = Column(String(80))
    lastname = Column(String(80))
    balance = Column(Float)


    def __str__(self):
        return f'Username: {self.firstname} {self.lastname}\nAccount balance: {self.balance}'

