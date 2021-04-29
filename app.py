from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Account(Base):
    __tablename__ = 'Accounts'

    id = Column(Integer, Sequence('account_id_seq'), primary_key=True)
    firstname = Column(String(80))
    lastname = Column(String(80))
    balance = Column(Float)


    def __str__(self):
        return f'Username: {self.firstname} {self.lastname}\nAccount balance: {self.balance}'

    ## method to check if the account exists, this is used as a complementary method
    def search_account(self, firstname, lastname):
        for row in session.query(Account.firstname, Account.lastname):
            if firstname in row and lastname in row:
                return True
            else:
                return False
    
    ## method to create an account and at the same time check if it already exists
    def create_account(self, firstname, lastname, starting_balance):
        if not self.search_account(firstname, lastname):
            new_user = Account(firstname=firstname, lastname=lastname, balance=starting_balance)
            session.add(new_user)
            session.commit()
            print("A sua conta foi criada com sucesso!")
            return True
        else:
            print("Ja existe uma conta com esse nome")
            return False


def create_account():
    firstname = str(input("Introduza o primeiro nome: "))
    lastname = str(input("Introduza o ultimo nome: "))
    starting_balance = float(input("Introduza o balance inicial"))

    if not search_users(firstname, lastname):
        Account.create_account(firstname, lastname, starting_balance)
    else:
        print("Conta nao e possivel")
        return False

## using the return from the cls method and checking
def search_users(firstname, lastname):
    if Account.search_account(firstname, lastname):
        print("Uma conta ja existe com esse nome")
        return True
    else:
        print("Conta disponivel para criacao")
        return False

def menu():
    print("Bem Vindo ao Banco do Aço")
    print("Introduza a opcao que pretende fazer")
    print("1 - Criar Conta\n2 - Depositar dinheiro na conta\n3 - Levantar dinheiro da conta")
    choice = input("Escolha -> ")
    if not int(choice):
        print("cant do that")
        return False
    else:
        choice = int(choice)
    
    return choice

rv_menu = menu()

create_account()
