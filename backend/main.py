from fastapi import FastAPI
from configs.config import URL
from lib.database.db import ConnectDB
from routers.user_router import router as UserRouter
from routers.auth_router import router as AuthRouter
from contextlib import asynccontextmanager
from models.user_model import User
from models.job_model import Job
from models.job_history_model import JobHistory
from models.notification_model import Notification
@asynccontextmanager
async def life_span(app:FastAPI):
    db_url = URL
    print(db_url)
    DBInstance = ConnectDB(db_url = db_url)
    DBInstance.connection()
    DBInstance.create_tables()

    app.state.engine = DBInstance.engine
    yield
    DBInstance.closeConnection()

app = FastAPI(lifespan=life_span)


@app.get('/health')
def root():
    return {"message":"Health is active"}


app.include_router(router=UserRouter)
app.include_router(router=AuthRouter)