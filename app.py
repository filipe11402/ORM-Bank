from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String, unique=True)
    balance = Column(Float)

    def __str__(self):
        return f'Account name: {self.name}\nTotal balance: {self.balance}'

