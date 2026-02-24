from sqlalchemy import select

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
    async def get_list(user_id, session):
        return (await session.execute(select(Note).where(Note.user_id==user_id))).scalars().all()
