from pydantic import BaseModel
import datetime
from sqlalchemy import Table, Column, String, Text, Date, ForeignKey
from . import metadata


class User(BaseModel):
    uuid: str
    email: str
    password_hash: str
    name: str
    photo: str | None
    role_id: int
    # role_name: str | None


class ResponseUser(BaseModel):
    uuid: str
    name: str
    photo: str | None
    role_id: int
    role_name: str | None


users_table = Table(
    'user',
    metadata,
    Column('uuid', String(128), primary_key=True, nullable=False),
    Column('name', String(128), nullable=False),
    Column('password_hash', String(40), nullable=False),
    Column('email', String(128), nullable=False, unique=True),
    Column('photo', Text),
    Column('role_id', ForeignKey("user_role.id"))
)
