import sqlalchemy
from app.db import entities, tokens_table, users_table, database, user_role_table, activity_table


async def get_all_activities() -> entities.User:
    query = sqlalchemy.select(activity_table,)

    result_rows = await database.fetch_all(query)

    return list(map(lambda row: entities.Activity.parse_obj(dict(row)), result_rows))

    # return entities.Activity\
    #     .parse_obj(dict(row_result))