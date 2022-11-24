import uvicorn
from fastapi import FastAPI

from crud.apis.v1.api import api_router
from crud.db.init_db import init_db

app = FastAPI()

app.include_router(api_router)

MAIN_APP_LOCATION = "crud.main:app"

if __name__ == "__main__":
    init_db()
    uvicorn.run(MAIN_APP_LOCATION, host="0.0.0.0", port=8000, reload=True)
