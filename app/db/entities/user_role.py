from pydantic import BaseModel
# from app.db import entities, users_table, database
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, insert
from . import metadata


class AuthToken(BaseModel):
    token: str
    owner_uuid: str


user_role_table = Table(
    'user_role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text)
)
    