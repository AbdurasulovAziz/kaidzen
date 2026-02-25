from sqlalchemy import select, update

from models import Note


class NoteRepository:

    @staticmethod
    async def create(data, session):
        new_obj = Note(**data, user_id=1)
        session.add(new_obj)
        await session.commit()
        await session.refresh(new_obj)
        return new_obj

    @staticmethod
    async def get_list(session):
        return (await session.execute(select(Note))).scalars().all()

    @staticmethod
    async def update(object_id, data, session):
        await session.execute(update(Note).where(Note.id == object_id).values(**data))
        await session.commit()

