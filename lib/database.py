from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection
DATABASE_URL = "sqlite:///theater.db"  # SQLite database

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Base class for models
Base = declarative_base()
