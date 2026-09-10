from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from database import engine

from routers.personel import router as personel_router

from routers.auth import router as auth_router

app = FastAPI(
    title="SIBER8 - YONIF",
    version="0.1.0",
    description="Backend aplikasi YONIF TP 807",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(personel_router)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "SIBER8 - YONIF",
    }


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
        }