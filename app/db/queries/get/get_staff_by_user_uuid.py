import sqlalchemy
from app.db import entities, tokens_table, users_table, database, user_role_table, activity_table, staff_table


async def get_staff_by_user_uuid(user_uuid) -> entities.Staff:
    query = sqlalchemy.select(staff_table).where(staff_table.c.user_id==user_uuid)

    result_rows = await database.fetch_one(query)

    return entities.Staff(**dict(result_rows))

    # return entities.Activity\
    #     .parse_obj(dict(row_result))