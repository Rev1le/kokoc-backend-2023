import sqlalchemy
from app.db import entities, users_table, database, staff_table


async def create_staff(user: entities.User):
    staff = entities.Staff(
        user_id=user.uuid,
        company_branch_id=1,
        balance=0
    )
    # values = user.dict()
    # values['role_id'] = 1

    query = sqlalchemy\
        .insert(staff_table)\
        .values(staff.dict())
    await database.execute(query)