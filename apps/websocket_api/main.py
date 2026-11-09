
from fastapi import FastAPI, WebSocket, WebSocketDisconnect


# --------------------------------------------------
# 1. Create FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="API Exploration Lab - WebSocket",
    description="Multi-client WebSocket Messaging API",
    version="1.0.0"
)


# --------------------------------------------------
# 2. Connection Manager
# --------------------------------------------------

class ConnectionManager:

    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    # Accept and register a new client
    async def connect(self, client_id: str, websocket: WebSocket):

        await websocket.accept()

        self.active_connections[client_id] = websocket

        print(f"{client_id} connected")

    # Remove a disconnected client
    def disconnect(self, client_id: str):

        if client_id in self.active_connections:
            del self.active_connections[client_id]

        print(f"{client_id} disconnected")

    # Send a message to all connected clients
    async def broadcast(self, message: dict):

        disconnected_clients = []

        for client_id, connection in list(
            self.active_connections.items()
        ):

            try:
                await connection.send_json(message)

            except Exception:
                disconnected_clients.append(client_id)

        # Remove connections that could not receive messages
        for client_id in disconnected_clients:
            self.disconnect(client_id)


# --------------------------------------------------
# 3. Create Connection Manager Object
# --------------------------------------------------

manager = ConnectionManager()


# --------------------------------------------------
# 4. WebSocket Endpoint
# --------------------------------------------------

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: str
):

    # Establish connection
    await manager.connect(client_id, websocket)

    # Notify all clients about the new connection
    await manager.broadcast({
        "event": "user_connected",
        "client_id": client_id,
        "message": f"{client_id} joined the chat"
    })

    try:

        while True:

            # Receive JSON message from client
            data = await websocket.receive_json()

            # Validate incoming message structure
            if not isinstance(data, dict) or "message" not in data:

                await websocket.send_json({
                    "event": "error",
                    "message": "Invalid message format"
                })

                continue

            message = data["message"]

            # Validate message content
            if not isinstance(message, str) or not message.strip():

                await websocket.send_json({
                    "event": "error",
                    "message": "Message cannot be empty"
                })

                continue

            # Broadcast message to all connected clients
            await manager.broadcast({
                "event": "new_message",
                "client_id": client_id,
                "message": message
            })

    except WebSocketDisconnect:

        # Remove disconnected client
        manager.disconnect(client_id)

        # Notify remaining clients
        await manager.broadcast({
            "event": "user_disconnected",
            "client_id": client_id,
            "message": f"{client_id} left the chat"
        })


# --------------------------------------------------
# 5. Root HTTP Endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Welcome to WebSocket API Exploration Lab",
        "websocket_endpoint": "/ws/{client_id}"
    }
