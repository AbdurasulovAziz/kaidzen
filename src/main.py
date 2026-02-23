from typing import Any

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from cors.database import get_db
from models import User

app = FastAPI(title="One-file FastAPI")

# =========================
# Routes
# =========================

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(payload: dict[str, Any], db: AsyncSession = Depends(get_db)):
    name = payload.get("name")

    if not isinstance(name, str) or not name.strip():
        raise HTTPException(status_code=400, detail="Field 'name' is required (non-empty string)")

    item = User(name=name.strip())
    db.add(item)
    await db.commit()
    await db.refresh(item)

    return {"id": item.id, "name": item.name}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)