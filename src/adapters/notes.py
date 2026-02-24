from datetime import timedelta, datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from cors.database import get_db
from domains.notes import NoteRepository
from models import Note

REPEATS = (
    timedelta(minutes=30),
    timedelta(days=1),
    timedelta(weeks=2),
    timedelta(weeks=4*3)
)

router = APIRouter()


class NoteBaseSchema(BaseModel):
    title: str

class NoteSchema(NoteBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int

@router.post(
    "/notes",
    response_model=NoteSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_note(
        payload: NoteBaseSchema,
        db: AsyncSession = Depends(get_db)
):
    return await NoteRepository.create(payload.model_dump(), db)

@router.get(
    "/notes",
    response_model=list[NoteSchema],
    status_code=status.HTTP_200_OK
)
async def get_notes(
        db: AsyncSession = Depends(get_db)
):
    return await NoteRepository.get_list(1, db)
