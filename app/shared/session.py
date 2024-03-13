
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# configure Session class with desired options
Session = sessionmaker()

# later, we create the engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/')

# associate it with our custom Session class
Session.configure(bind=engine)

# work with the session
session = Session()