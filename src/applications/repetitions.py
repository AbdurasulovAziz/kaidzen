from datetime import timedelta, datetime

from domains.repetitions import RepetitionRepository

REPEATS = (
    timedelta(minutes=30),
    timedelta(days=1),
    timedelta(weeks=2),
    timedelta(weeks=4*3)
)

class RepetitionService:

    @staticmethod
    async def create_repetition(data, session):

        last_repetition_iteration = await RepetitionRepository.get_last_repetitions_iteration_by_id(data.note_id, session) or 0

        last_index = len(REPEATS) - 1

        if last_repetition_iteration > last_index:
            next_review_at = datetime.now() + REPEATS[last_index]
        else:
            next_review_at = datetime.now() + REPEATS[last_repetition_iteration]

        new_repetition = await RepetitionRepository.create(
            data.model_dump() | {"iteration": last_repetition_iteration + 1, "next_review_at": next_review_at},
            session
        )

        return new_repetition
