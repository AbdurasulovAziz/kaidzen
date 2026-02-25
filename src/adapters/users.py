from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from cors.database import get_db
from domains.users import UserRepository

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

    return await UserRepository.create(payload.model_dump(), db)

@router.get(
    "/users",
    response_model=list[UserSchema],
    status_code=status.HTTP_200_OK
)
async def get_users(
        db: AsyncSession = Depends(get_db)
):
    return await UserRepository.get_list(db)
