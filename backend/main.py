
from fastapi import FastAPI
from sqlalchemy import text

from database import engine
from pydantic import BaseModel

app = FastAPI()

class PlayerCreate(BaseModel):
	name: str

@app.get("/")
def root():
    return {"message": "Welcome to DartReplay"}


@app.get("/players")
def get_players():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM players")
        )

        players = []

        for row in result:
            players.append(
                {
                    "id": row.id,
                    "name": row.name
                }
            )

        return players

@app.post("/players")
def create_player(player: PlayerCreate):
    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO players (name) VALUES (:name)"
            ),
            {"name": player.name}
        )

        connection.commit()

    return {
        "message": "Player created",
        "name": player.name
    }

