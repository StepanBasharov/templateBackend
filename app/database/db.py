from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DefaultConfig

engine = create_engine(DefaultConfig.db_url)
ORMSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
