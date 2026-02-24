from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from cors.database import get_db
from models import Note, User

router = APIRouter()


class UserBaseSchema(BaseModel):
    name: str

class UserSchema(UserBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int

@router.post(
    "/users",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
        payload: UserBaseSchema,
        db: AsyncSession = Depends(get_db)
):
    new_note = Note(title=payload.title, user_id=payload.user_id)
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)

    return new_note

@router.get(
    "/users",
    response_model=list[UserSchema],
    status_code=status.HTTP_200_OK
)
async def get_users(
        db: AsyncSession = Depends(get_db)
):
    return (await db.execute(select(User))).scalars().all()
