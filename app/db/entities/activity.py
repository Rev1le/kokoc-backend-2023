from pydantic import BaseModel
import datetime
from sqlalchemy import Table, Column, String, Text, Date, ForeignKey, Integer
from . import metadata


class Activity(BaseModel):
    id: int
    name: str
    index: int


class ResponseActivity(BaseModel):
    id: int
    name: str
    index: int


activity_table = Table(
    'activity',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    Column('name', String(128), nullable=False),
    Column('index', Integer, nullable=False),
)
