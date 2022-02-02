from Pegasus_System import MONGO_CLIENT
from datetime import datetime
from random import choice

db = MONGO_CLIENT["Pegasus"]["Main"]


async def get_data() -> dict:
    data = await db.find_one({"_id": 4})
    return data


async def add_inspector(Master: int, inspector: int) -> True:
    data = await get_data()
    data["data"][str(Master)][str(inspector)] = []
    data["standalone"][str(inspector)] = {
        "addedby": Master,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)


async def add_enforcers(inspector: int, enforcer: int) -> True:
    data = await get_data()
    Lovely = data["standalone"][str(inspector)]["addedby"]
    if Lovely == 777000:
        s = data["data"][str(inspector)]
        s[list(choice(s.keys()))].append([enforcer])
    else:
        data["data"][str(Lovely)][str(inspector)].append([enforcer])
    data["standalone"][str(enforcer)] = {
        "addedby": inspector,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)
