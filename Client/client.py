
import asyncio
import websockets
import json

async def connect():
    uri = "wss://yokinetwork.onrender.com/ws"

    async with websockets.connect(uri) as ws:
        response = await ws.recv()
        print("SERVER:", response)

        await ws.send(json.dumps({
            "event": "hello",
            "message": "Hello YokiNetwork!"
        }))

        response = await ws.recv()
        print("SERVER:", response)

asyncio.run(connect())
