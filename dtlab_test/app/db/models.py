#BASE MODELS FOR SQLALCHEMY
#app/db/models.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base #Base is the declarative base defined in session.py

#Equivalent to a JPA Entity for user
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    #Relationship: one User can own many servers
    servers = relationship("Server", back_populates="owner")
    
#Equivalent to a JPA Entity for Server
class Server(Base):
    __tablename__ = "servers"
    
    #server_ulid is the unique identifier generated by the by the backend
    server_ulid = Column(String, primary_key=True, index=True)
    server_name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    #RelationShip= one server can have many sensor data entries (@ManyToOne)
    sensor_data = relationship("SensorData", back_populates="server")
    
    #RelationShip= back reference to the owning user
    owner = relationship("User", back_populates="servers")


#Equivalent to a JPA Entity for Sensor Data
class SensorData(Base):
    __tablename__="sensor_data"
    
    id = Column(Integer, primary_key=True, index=True)
    server_ulid = Column(String, ForeignKey("servers.server_ulid"), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    voltage = Column(Float, nullable=True)
    current = Column(Float, nullable=True)
    
    #Relationship= link back to the server that sent the data
    server = relationship("Server", back_populates="sensor_data")
    
    

    