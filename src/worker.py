import asyncio

from cors.database import SessionLocal
from domains.repetitions import RepetitionRepository


async def get_repetable_data():
    async with SessionLocal() as session:
        objects = await RepetitionRepository.get_list(session)
        for obj in objects:
            print(obj)



async def worker_loop():
    while True:
        try:
            await get_repetable_data()
        except Exception as e:
            print("Worker error:", e)

        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(worker_loop())