import sqlalchemy
from app.db import entities, users_table, database


async def create_user(user: entities.User):
    values = user.dict()
    values['role_id'] = 1

    query = sqlalchemy\
        .insert(users_table)\
        .values(values)
    await database.execute(query)