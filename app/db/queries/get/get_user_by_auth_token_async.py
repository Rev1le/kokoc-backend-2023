import sqlalchemy
from app.db import entities, tokens_table, users_table, database, user_role_table


async def get_user_by_auth_token(auth_token: str) -> entities.User:
    query = sqlalchemy\
        .select(users_table, user_role_table.c.name.label('role_name'))\
        .join(
            users_table,
            tokens_table.c.owner_uuid == users_table.c.uuid,
            isouter=True
        )\
        .join(
            user_role_table,
            user_role_table.c.id == users_table.c.role_id,
            isouter=True
        )\
        .where(tokens_table.c.token == auth_token)

    print("QUERY =======>", query)

    row_result = await database.fetch_one(query)

    if row_result is None: 
        return row_result

    return entities.User\
        .parse_obj(dict(row_result))