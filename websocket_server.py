from fastapi import FastAPI, WebSocket, WebSocketDisconnect

ws_app = FastAPI()

@ws_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

# cmd : uvicorn app.websocket_server:ws_app --port 9000


# cmd : uvicorn app.tts_ws:app --port 9000
