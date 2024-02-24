from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import null


class Device(BaseModel):
    user_id: Optional[int] = None


class User(BaseModel):
    username: str


class Data(BaseModel):
    device_id: int
    x: float = Field(ge=0)
    date: datetime


class Statistics(BaseModel):
    value: str
    device_id: int
    min: float
    max: float
    count: int
    sum: float
    percentile_cont: float


