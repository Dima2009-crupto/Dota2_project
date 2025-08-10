import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

#from app.db.base import create_db
from app.routes.users import users_route
from app.routes.teams import teams_router
from app.routes.tournaments import tournaments_router
from app.db.base import create_db


app = FastAPI(root_path="/api")
app.include_router(users_route)
app.include_router(teams_router)
app.include_router(tournaments_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    # asyncio.run(create_db())
    uvicorn.run("main:app", reload=True)