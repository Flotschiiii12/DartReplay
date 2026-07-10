from sqlalchemy import create_engine

DATABASE_URL = "postgresql://dartreplay:dartreplay123@localhost:5432/dartreplay"

engine = create_engine(DATABASE_URL)
