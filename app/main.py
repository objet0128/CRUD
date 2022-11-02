import uvicorn
from fastapi import FastAPI

from app.db.init_db import init_db

app = FastAPI()

init_db()

if __name__ == "__main__":
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)
