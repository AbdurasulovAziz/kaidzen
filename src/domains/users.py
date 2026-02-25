from sqlalchemy import select

from models import User


class UserRepository:

    @staticmethod
    async def create(data, session):
        new_obj = User(**data)
        session.add(new_obj)
        await session.commit()
        await session.refresh(new_obj)
        return new_obj

    @staticmethod
    async def get_list(session):
        return (await session.execute(select(User))).scalars().all()

