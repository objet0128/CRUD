import uvicorn
from fastapi import FastAPI

from app.apis.api import api_router
from app.db.init_db import call_init_db

app = FastAPI(callbacks=call_init_db())

app.include_router(api_router)

MAIN_APP_LOCATION = "app.main:app"

if __name__ == "__main__":
    uvicorn.run(MAIN_APP_LOCATION, host="0.0.0.0", port=8000, reload=True)
