from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Float, create_engine

metadata = MetaData()
engine = create_engine('sqlite:///task.db', echo=True)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, nullable=False, unique=True),
)

device = Table(
    "device",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=True),
)

data = Table(
    "data",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("x", Float),
    Column("device_id", Integer, ForeignKey("device.id"), nullable=False),
    Column("date", TIMESTAMP, default=datetime.utcnow),
)

metadata.create_all(engine)
