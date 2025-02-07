#Used to create a database engine, which is the core interface to the database. It manages the connection pool and executes SQL statements.
from sqlalchemy import create_engine 
#Used to create a base class for ORM models. This base class is later used to define database tables as Python classes.
from sqlalchemy.ext.declarative import declarative_base
#Used to create a session factory, which is responsible for creating sessions to interact with the database.
from sqlalchemy.orm import sessionmaker

# Database connection URL
DATABASE_URL = "postgresql://postgres:medall@localhost:5432/insurance_medical"

# Create the database engine
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connected to the database successfully!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

# Session factory and Base setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()