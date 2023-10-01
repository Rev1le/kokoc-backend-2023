import sqlite3
import databases
import sqlalchemy

from sqlalchemy import insert

from app.db.entities import *

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


async def save_insert(stmt):
    try:
        await database.execute(stmt)
    except sqlite3.IntegrityError:
        pass

#Migrations

async def create_user_role_table_migrations():
    stmt = insert(user_role_table).values(name="Сотрудник компании", id=1)
    await save_insert(stmt)

    stmt = insert(user_role_table).values(name="Руководитель компании", id=2)
    await save_insert(stmt)

    stmt = insert(user_role_table).values(name="руководитель проекта", id=3)
    await save_insert(stmt)

async def create_activity_table_migrations():
    stmt = insert(activity_table).values(name="Прогулка", id=1, index=10)
    await save_insert(stmt)

    stmt = insert(activity_table).values(name="Велопрогулка", id=2, index=2)
    await save_insert(stmt)

    stmt = insert(activity_table).values(name="Пробежка", id=3, index=20)
    await save_insert(stmt)

    stmt = insert(activity_table).values(name="Заплыв", id=4, index=30)
    await save_insert(stmt)


async def startup():
    await database.connect()
    await create_user_role_table_migrations()
    await create_activity_table_migrations()


async def shutdown():
    await database.disconnect()
