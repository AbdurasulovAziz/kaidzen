from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from cors.database import get_db
from models import Note, Repetition

router = APIRouter()


class RepetitionBaseSchema(BaseModel):
    title: str
    user_id: int

class RepetitionSchema(RepetitionBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int

@router.post(
    "/repetitions",
    response_model=RepetitionSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_repetition(
        payload: RepetitionBaseSchema,
        db: AsyncSession = Depends(get_db)
):
    ...
    # new_note = Note(title=payload.title, user_id=payload.user_id)
    # db.add(new_note)
    # await db.commit()
    # await db.refresh(new_note)

    # return new_note

@router.get(
    "/repetitions",
    response_model=list[RepetitionSchema],
    status_code=status.HTTP_200_OK
)
async def get_notes(
        db: AsyncSession = Depends(get_db)
):
    return (await db.execute(select(Repetition))).scalars().all()
