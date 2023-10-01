from pydantic import BaseModel
import datetime
from sqlalchemy import Table, Column, String, Text, Date, ForeignKey, Integer
from . import metadata


# class User(BaseModel):
#     uuid: str
#     email: str
#     password_hash: str
#     name: str
#     photo: str | None


# class ResponseUser(BaseModel):
#     uuid: str
#     name: str
#     photo: str | None
#     role_id: int


ceo_table = Table(
    'ceo',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    Column('user_uuid', ForeignKey('user.uuid'), nullable=False),
    Column('company_id', ForeignKey('company.id'), nullable=False),
)
