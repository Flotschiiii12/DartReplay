from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    average = Column(Float)
    checkout_percentage = Column(Float)
    hundred_eighty_count = Column(Integer)

from sqlalchemy import Boolean


class Throw(Base):
    __tablename__ = "throws"

    id = Column(Integer, primary_key=True)

    sector = Column(String)
    x = Column(Integer)
    y = Column(Integer)

    bounceout = Column(Boolean)

    detection_time = Column(String)

class Highlight(Base):
    __tablename__ = "highlights"

    id = Column(Integer, primary_key=True)

    highlight_type = Column(String)

    created_at = Column(String)

class ReplayTrigger(Base):
    __tablename__ = "replay_triggers"

    id = Column(Integer, primary_key=True)

    highlight_id = Column(Integer)

    trigger_type = Column(String)

    created_at = Column(String)

class ReplayQueue(Base):
    __tablename__ = "replay_queue"

    id = Column(Integer, primary_key=True)

    trigger_id = Column(Integer)

    status = Column(String)

    created_at = Column(String)
