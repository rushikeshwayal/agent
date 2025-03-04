from sqlalchemy import Column, Integer, Text, Float, ARRAY
from sqlalchemy.dialects.postgresql import ARRAY as PG_ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import declarative_base
from database import engine, Base  # Import Base from database.py

# Define ORM model for the table
class DomainEmbedding(Base):
    __tablename__ = "domain_embeddings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain_name = Column(Text, nullable=False)
    domain_description = Column(Text, nullable=False)
    keywords = Column(PG_ARRAY(Text), nullable=False)  # PostgreSQL Array of Text
    confidence_score = Column(Float, nullable=False)
    embedding = Column(PG_ARRAY(Float), nullable=False)  # Storing as array in PostgreSQL

# Create tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

# Run the table creation if executed directly
if __name__ == "__main__":
    init_db()
