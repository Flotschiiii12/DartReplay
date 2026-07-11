
from fastapi import FastAPI
from sqlalchemy import text

from database import engine
from pydantic import BaseModel

app = FastAPI()

class PlayerCreate(BaseModel):
	name: str

class MatchCreate(BaseModel):
	player_id: int
	average: float
	checkout_percentage: float
	hundred_eighty_count: int

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



@app.get("/matches")
def get_matches():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM matches")
        )

        matches = []

        for row in result:
            matches.append(
                {
                    "id": row.id,
                    "player_id": row.player_id,
                    "average": row.average,
                    "checkout_percentage": row.checkout_percentage,
                    "hundred_eighty_count": row.hundred_eighty_count
                }
            )

        return matches


@app.post("/matches")
def create_match(match: MatchCreate):
    with engine.connect() as connection:
        connection.execute(
            text("""
                INSERT INTO matches (
                    player_id,
                    average,
                    checkout_percentage,
                    hundred_eighty_count
                )
                VALUES (
                    :player_id,
                    :average,
                    :checkout_percentage,
                    :hundred_eighty_count
                )
            """),
            {
                "player_id": match.player_id,
                "average": match.average,
                "checkout_percentage": match.checkout_percentage,
                "hundred_eighty_count": match.hundred_eighty_count
            }
        )

        connection.commit()

    return {"message": "Match created"}

@app.get("/stats")
def get_stats():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    p.name,
                    m.average,
                    m.checkout_percentage,
                    m.hundred_eighty_count
                FROM matches m
                JOIN players p
                    ON p.id = m.player_id
            """)
        )

        stats = []

        for row in result:
            stats.append(
                {
                    "player": row.name,
                    "average": row.average,
                    "checkout_percentage": row.checkout_percentage,
                    "hundred_eighty_count": row.hundred_eighty_count
                }
            )

        return stats

@app.get("/throws")
def get_throws():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM throws ORDER BY id DESC LIMIT 100")
        )

        throws = []

        for row in result:
            throws.append(
                {
                    "id": row.id,
                    "sector": row.sector,
                    "x": row.x,
                    "y": row.y,
                    "bounceout": row.bounceout,
                    "detection_time": row.detection_time
                }
            )

        return throws

@app.get("/throw-stats")
def get_throw_stats():
    with engine.connect() as connection:

        total = connection.execute(
            text("SELECT COUNT(*) FROM throws")
        ).scalar()

        doubles = connection.execute(
            text(
                "SELECT COUNT(*) FROM throws WHERE sector LIKE 'D%'"
            )
        ).scalar()

        trebles = connection.execute(
            text(
                "SELECT COUNT(*) FROM throws WHERE sector LIKE 'T%'"
            )
        ).scalar()

        bounceouts = connection.execute(
            text(
                "SELECT COUNT(*) FROM throws WHERE bounceout = true"
            )
        ).scalar()

        singles = total - doubles - trebles

        return {
            "total_throws": total,
            "single_hits": singles,
            "double_hits": doubles,
            "treble_hits": trebles,
            "bounceouts": bounceouts
        }
@app.get("/highlights")
def get_highlights():
    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT *
                FROM throws
                ORDER BY id DESC
                LIMIT 3
            """)
        )

        throws = list(result)

        if len(throws) < 3:
            return {
                "highlight_detected": False
            }

        sectors = [
            throws[0].sector,
            throws[1].sector,
            throws[2].sector
        ]

        if sectors == ["T20", "T20", "T20"]:
            return {
                "highlight_detected": True,
                "type": "180"
            }

        return {
            "highlight_detected": False
        }
