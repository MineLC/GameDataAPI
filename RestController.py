from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class GameData(BaseModel):
    players: list[str]
    changed_blocks: list[str]
    join: list[str]
    quit: list[str]

minecraft_data = GameData(players=[], changed_blocks=[], join=[], quit=[])
roblox_data = GameData(players=[], changed_blocks=[], join=[], quit=[])

@app.get("/v1/mcsrv/")
async def get_spigot_data():
    # Retorna los datos acumulados para ser consumidos por Roblox
    return minecraft_data.dict()

@app.post("/v1/mcsrv/")
async def receive_spigot_data(data: GameData):
    # Procesa los datos recibidos desde Spigot
    minecraft_data.players.extend(data.players)
    minecraft_data.changed_blocks.extend(data.changed_blocks)
    minecraft_data.join.extend(data.join)
    minecraft_data.quit.extend(data.quit)
    return {"message": "Data received successfully from Spigot"}

@app.get("/v1/rbxsrv/")
async def get_roblox_data():
    # Retorna los datos acumulados para ser consumidos por Roblox
    return roblox_data.dict()

@app.post("/v1/rbxsrv/")
async def receive_roblox_data(data: GameData):
    # Procesa los datos recibidos desde Roblox
    roblox_data.players.extend(data.players)
    roblox_data.changed_blocks.extend(data.changed_blocks)
    roblox_data.join.extend(data.join)
    roblox_data.quit.extend(data.quit)
    return {"message": "Data received successfully from Roblox"}