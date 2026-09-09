from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth,health,organizations
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
import app.models
@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn: await conn.run_sync(Base.metadata.create_all)
    yield
app=FastAPI(title=settings.APP_NAME,version="2.0.0-foundation",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origins_list,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(health.router)
app.include_router(auth.router,prefix=settings.API_V1_PREFIX)
app.include_router(organizations.router,prefix=settings.API_V1_PREFIX)
@app.get("/")
async def root(): return {"name":settings.APP_NAME,"version":"2.0.0-foundation","docs":"/docs"}
