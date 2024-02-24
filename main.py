from datetime import datetime
from fastapi import FastAPI
from sqlalchemy import insert, select, func, update
from models.models import engine, user, device, data
from schemas import Statistics, Device, Data, User

app = FastAPI(
    title='App'
)


@app.get('/devices/{device_id}/')
def get_device(device_id: int):
    conn = engine.connect()
    stmt = (
        device.select()
        .where(device.c.id == device_id)
    )
    res = conn.execute(stmt)
    res_data = list(res.mappings())
    return {'res_data': res_data}


@app.post('/devices/add-device/')
def add_device(new_device: Device):
    conn = engine.connect()
    stmt = insert(device).values(**new_device.dict())
    conn.execute(stmt)
    conn.commit()
    return {'status': 'success'}


@app.get('/statistics/')
def get_data(device_id: int):
    conn = engine.connect()
    stmt = (
        select(
            data.c.device_id,
            func.min(data.c.x), func.max(data.c.x),
            func.count(), func.sum(data.c.x))
        .where(data.c.device_id == device_id)
    )
    res = conn.execute(stmt)

    stmt2 = (
        select(data.c.x)
        .where(data.c.device_id == device_id)
        .order_by(data.c.x)
    )
    res2 = conn.execute(stmt2)
    data_table = list(res2.scalars())
    n = len(data_table)
    res_data = []
    if n >= 1:
        median = (data_table[n//2 - 1] + data_table[n//2]) / 2 if n % 2 == 0 else data_table[n//2]
        res_data = {**{'value': 'x'}, **dict(list(res.mappings())[0]), **{'median': median}}
    return {'status': 'success', 'res_data': res_data}


@app.get('/statistics/certain-period/')
def get_data_certain_period(device_id: int, date_start: datetime, date_end: datetime):
    conn = engine.connect()
    stmt = (
        select(
            data.c.device_id,
            func.min(data.c.x), func.max(data.c.x),
            func.count(), func.sum(data.c.x)
        )
        .where(data.c.device_id == device_id)
        .filter(data.c.date.between(date_start, date_end))
    )
    res = conn.execute(stmt)

    stmt2 = (
        select(data.c.x)
        .where(data.c.device_id == device_id)
        .filter(data.c.date.between(date_start, date_end))
        .order_by(data.c.x)
    )
    res2 = conn.execute(stmt2)
    data_table = list(res2.scalars())
    n = len(data_table)
    res_data = []
    if n >= 1:
        median = (data_table[n//2 - 1] + data_table[n//2]) / 2 if n % 2 == 0 else data_table[n//2]
        res_data = {**{'value': 'x'}, **dict(list(res.mappings())[0]), **{'median': median}}
    return {'status': 'success', 'res_data': res_data}


@app.post('/statistics/add-data/')
def add_data(new_data: Data):
    conn = engine.connect()
    stmt = insert(data).values(**new_data.dict())
    conn.execute(stmt)
    conn.commit()
    return {'status': 'success'}


@app.get('/users/{user_id}/')
def get_user(user_id: int):
    conn = engine.connect()
    stmt = (
        user.select()
        .where(user.c.id == user_id)
    )
    res = conn.execute(stmt)
    res_data = list(res.mappings())
    return {'status': 'success', 'res_data': res_data}


@app.post('/users/add-user/')
def add_user(new_user: User):
    conn = engine.connect()
    stmt = insert(user).values(**new_user.dict())
    conn.execute(stmt)
    conn.commit()
    return {'status': 'success'}


@app.post('/devices/{device_id}/add-user/')
def add_device_user(device_id: int, user_id: int):
    conn = engine.connect()
    stmt = (
        update(device)
        .where(device.c.id == device_id)
        .values(user_id=user_id)
    )
    conn.execute(stmt)
    conn.commit()
    return {'status': 'success'}


@app.get('/statistics/by-user/')
def get_user_data(user_id: int, device_id: int = None):
    conn = engine.connect()
    stmt = (
        select(
            data.c.device_id,
            func.min(data.c.x), func.max(data.c.x),
            func.count(), func.sum(data.c.x))
        .select_from(
            data.join(device, device.c.id == data.c.device_id)
                .join(user, device.c.user_id == user.c.id)
        )
        .where(user.c.id == user_id)
    )
    if device_id is not None:
        stmt = stmt.where(device.c.id == device_id)
    res = conn.execute(stmt)

    stmt2 = (
        select(data.c.x)
        .select_from(
            data.join(device, data.c.device_id == device.c.id)
                .join(user, device.c.user_id == user.c.id)
        )
        .where(user.c.id == user_id)
        .order_by(data.c.x)
    )
    if device_id is not None:
        stmt2 = stmt2.where(device.c.id == device_id)
    res2 = conn.execute(stmt2)
    data_table = list(res2.scalars())
    n = len(data_table)
    res_data = []
    if n >= 1:
        median = (data_table[n//2 - 1] + data_table[n//2]) / 2 if n % 2 == 0 else data_table[n//2]
        res_data = {**{'value': 'x'}, **dict(list(res.mappings())[0]), **{'median': median}}
    return {'status': 'success', 'res_data': res_data}


