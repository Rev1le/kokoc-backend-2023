import uuid
import hashlib
import sqlite3
from datetime import datetime, timezone
from app.db.queries.get.get_staff_by_user_uuid import get_staff_by_user_uuid
from app.db.queries.get.get_all_activities import get_all_activities

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


from app.api.deps import GetLogger
from app import db
from app.api.deps import AuthUser
from app.db import entities
from app.db.queries.create.create_activity_log import create_activity_log as create_activity_log_query
# from app.db.queries.create.create_auth_token_async import create_auth_token
# from app.db.queries.get.get_user_by_email_password_hash_async import get_user_by_email_password_hash

router = APIRouter()

class LogData(BaseModel):
    activity_id: int
    activity_index: int
    meter_amount: int


@router.get("/")
async def get_activities(user: AuthUser, logger: GetLogger) -> list[entities.Activity]:
    activities = await get_all_activities()
    return activities


@router.post("/log")
async def create_activity_log(user: AuthUser, logger: GetLogger, log_data: LogData) -> None:

    staff = await get_staff_by_user_uuid(user.uuid)

    log = entities.ActivityLog(
        datetime=datetime.now(),
        **log_data.dict(),
        coin_amount='',
        staff_id=staff.id
    )
    await create_activity_log_query(log)

    return None