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


staff_table = Table(
    'staff',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    Column('user_id', ForeignKey('user.uuid'), nullable=False),
    Column('company_branch_id', ForeignKey('company_branch.id'), nullable=False),
    Column('balance', Integer, nullable=False),
    Column('fund_id', ForeignKey('fund.id'), nullable=False),
)