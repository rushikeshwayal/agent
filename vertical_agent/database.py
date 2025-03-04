from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user = "postgres"
password = "newpassword"
host = "127.0.0.1"
port = "5432"
database = "vect"
# Database connection URL
DATABASE_URL = f'postgresql://postgres:{password}@{host}:{port}/{database}'

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
