from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PythonEnum
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

Base = declarative_base()

class StatusEnum(PythonEnum):
    started = 'started'
    error = 'error'
    stopped = 'stopped'
    unauthorized = 'unauthorized'

class Camera(Base):
    _tablename_ = 'camera'
    Id = Column(Integer, primary_key=True)
    CameraSecurityId = Column(String, unique=True)
    Name = Column(String, unique=True)
    NormalizedCameraName = Column(String, nullable=True)
    RtspUrl = Column(String)
    CompanyName = Column(String, nullable=True)
    IsWideViewCamera = Column(String, nullable=True)
    ModelNo = Column(String, nullable=True)
    Width = Column(String, nullable=True)
    Height = Column(String, nullable=True)
    Fps = Column(Integer, nullable=True)
    HorizontalDepth = Column(String, nullable=True)
    TcpConnection = Column(Boolean)
    Status = Column(Enum(StatusEnum), default=StatusEnum.stopped)
    DecodeTopic = Column(String, nullable=True, unique=True)
    LocationId = Column(Integer, nullable=True)
    CustomerId = Column(Integer, nullable=True)
    Roi = Column(String, nullable=True)
    Line = Column(String, nullable=True)
    Direction = Column(String, nullable=True)
    CreatedBy = Column(Integer, nullable=True)
    AnalyticsTypeId = Column(Integer, nullable=True)
    CreatedAt = Column(DateTime, nullable=False)
    UpdatedBy = Column(Integer, nullable=True)
    UpdatedAt = Column(DateTime, nullable=False)

    Analytics = relationship("Analytics", back_populates="Camera")
    AnalyticsType = relationship("Rules", back_populates="Cameras")
    Customer = relationship("Customer", back_populates="Cameras")
    Address = relationship("Location", back_populates="Cameras")

class Analytics(Base):
    pass;
    # Define your Analytics model

class Rules(Base):
    pass
    # Define your Rules model

class Customer(Base):
    pass
    # Define your Customer model

class Location(Base):
    pass
    # Define your Location model

Camera_Pydantic = sqlalchemy_to_pydantic(Camera)
CameraCreate_Pydantic = sqlalchemy_to_pydantic(Camera, exclude=['Id'])