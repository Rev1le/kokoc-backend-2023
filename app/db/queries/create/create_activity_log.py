import secrets
from app.db import entities, tokens_table, database


async def create_activity_log(log: entities.ActivityLog):
    # auth_token = entities.AuthToken(
    #     token=secrets.token_urlsafe(32),
    #     owner_uuid=user_uuid
    # )

    query = tokens_table \
        .insert() \
        .values(log.dict())

    await database.execute(query)