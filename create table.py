import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Setup database connection URI
DATABASE_URI = "mysql+pymysql://freedb_admin-user:437Wa4Jbj%SQe?d@sql.freedb.tech:3306/freedb_ngl-clonedatabase"

# Create an engine and session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Define the Message model (table)
class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message = Column(String(500), nullable=False)
    ip = Column(String(50), nullable=False)
    device_type = Column(String(50))
    os = Column(String(50))
    browser = Column(String(50))
    screen_size = Column(String(50))
    city = Column(String(50))
    region = Column(String(50))
    isp_name = Column(String(50))
    connection_type = Column(String(50))

# Create the table
try:
    Base.metadata.create_all(engine)
    print("Table 'message' created successfully!")
except Exception as e:
    print(f"Error: {e}")
