from datetime import timedelta, datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from applications.repetitions import RepetitionService
from cors.database import get_db
from models import Repetition

router = APIRouter()


class RepetitionBaseSchema(BaseModel):
    text: str
    note_id: int


class RepetitionSchema(RepetitionBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int
    iteration: int
    next_review_at: datetime

@router.post(
    "/repetitions",
    response_model=RepetitionSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_repetition(
        payload: RepetitionBaseSchema,
        db: AsyncSession = Depends(get_db)
):
    return await RepetitionService.create_repetition(payload, db)

@router.get(
    "/repetitions",
    response_model=list[RepetitionSchema],
    status_code=status.HTTP_200_OK
)
async def get_repetitions(
        db: AsyncSession = Depends(get_db)
):
    return (await db.execute(select(Repetition))).scalars().all()
