
from fastapi import FastAPI, WebSocket
from datetime import datetime

app = FastAPI(
    title="YokiNetwork",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "name": "YokiNetwork",
        "status": "online",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    await ws.send_json({
        "event": "connected",
        "message": "Connected to YokiNetwork!"
    })

    try:
        while True:
            data = await ws.receive_json()

            await ws.send_json({
                "event": "message",
                "data": data,
                "timestamp": datetime.now().isoformat()
            })

    except Exception:
        pass
