import uvicorn
from fastapi import FastAPI

from adapters.notes import router as note_routers
from adapters.repetitions import router as repetition_routers
from adapters.users import router as user_routers




app = FastAPI(title="One-file FastAPI")

app.include_router(note_routers)
app.include_router(repetition_routers)
app.include_router(user_routers)


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
