from pydantic import BaseModel
import datetime
from sqlalchemy import Table, Column, String, Text, Date, ForeignKey, Integer
from . import metadata


class User(BaseModel):
    uuid: str
    email: str
    password_hash: str
    name: str
    photo: str | None


class ResponseUser(BaseModel):
    uuid: str
    name: str
    photo: str | None
    role_id: int


activity_log_table = Table(
    'activity_log',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    Column('datetime', Date, nullable=False),
    Column('activity_id', ForeignKey('activity.id'), nullable=False),
    Column('activity_index', ForeignKey('activity.index'), nullable=False),
    Column('coin_amount', Integer, nullable=False),
    Column('staff_id', ForeignKey('staff.id'), nullable=False),
    Column('meter_amount', Integer, nullable=False)
)
