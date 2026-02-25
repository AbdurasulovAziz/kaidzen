from sqlalchemy import select, update, desc

from models import Repetition


class RepetitionRepository:

    @staticmethod
    async def create(data, session):
        new_obj = Repetition(**data)
        session.add(new_obj)
        await session.commit()
        await session.refresh(new_obj)
        return new_obj

    @staticmethod
    async def get_list(session):
        return (await session.execute(select(Repetition))).scalars().all()

    @staticmethod
    async def get_last_repetitions_iteration_by_id(note_id, session):
        return (await session.execute(select(Repetition.iteration).where(Repetition.note_id == note_id).order_by(desc(Repetition.iteration)))).scalars().first()


