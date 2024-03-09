from util import *
from fastapi import FastAPI
from pydantic import BaseModel


class TeamInformation(BaseModel):
    user: str
    team: list


app = FastAPI()


@app.get("/api/teams")
async def teams():
    return get_all_teams()


@app.get("/api/teams/{user}")
async def teams_user(user: str):
    return get_user_teams(user)


@app.post("/api/teams")
async def teams_create(team_information: TeamInformation):
    return create_team(team_information.model_dump())
