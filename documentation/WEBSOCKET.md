# WebSocket API

## 1. Overview

WebSocket is a communication protocol that enables two-way communication between a client and a server over a single, persistent TCP connection.

Unlike traditional HTTP request-response communication, WebSocket allows both the client and server to send messages independently after the connection is established.

It is commonly used in applications that require real-time communication.

## 2. Purpose

WebSocket is designed to provide continuous, bidirectional communication between applications.

Its main purposes are:

- Enable real-time data exchange.
- Support two-way communication.
- Maintain a persistent connection.
- Reduce repeated HTTP requests.
- Deliver messages instantly between connected clients and servers.

## 3. Core Components

| Component | Description |
|---|---|
| WebSocket Client | Application that initiates and maintains the connection. |
| WebSocket Server | Accepts connections and handles incoming messages. |
| Handshake | Initial HTTP-based process used to establish a WebSocket connection. |
| Connection | Persistent communication channel between client and server. |
| Messages | Data exchanged between the client and server. |
| Frames | Units used to transfer WebSocket data. |
| Connection Manager | Manages active client connections. |
| Event Handler | Processes incoming messages and connection events. |

## 4. Architecture

WebSocket follows a bidirectional client-server communication architecture.

```text id="wsflow1"
          Client 1
              |
              | WebSocket Connection
              |
              v
       WebSocket Server
              |
       Connection Manager
              |
              |
       Message Broadcasting
              |
          Client 2
```

**Main flow:**

1. The client sends an HTTP Upgrade request.
2. The server accepts the WebSocket handshake.
3. A persistent WebSocket connection is established.
4. The client and server exchange messages.
5. The server can broadcast messages to multiple connected clients.
6. The connection closes when either side disconnects.

## 5. Internal Working

WebSocket works through the following steps:

1. **Connection Request:** The client initiates a connection using a WebSocket URL.
2. **Handshake:** An HTTP request is sent with an Upgrade header requesting a protocol switch.
3. **Connection Establishment:** The server accepts the handshake and upgrades the connection.
4. **Message Exchange:** Both client and server can send messages independently.
5. **Message Processing:** The server receives and processes incoming messages.
6. **Broadcasting:** The server can distribute a message to multiple connected clients.
7. **Disconnection:** Either side can close the connection.

After the handshake, communication continues using the WebSocket protocol instead of separate HTTP requests.

## 6. Functions and Features

**Important WebSocket functions and features:**

- **Full-Duplex Communication:** Client and server can communicate simultaneously.
- **Persistent Connection:** Maintains an active connection for continuous communication.
- **Handshake:** Establishes the WebSocket connection through an HTTP Upgrade request.
- **Message Sending:** Allows both sides to send messages.
- **Message Receiving:** Receives messages without creating a new HTTP request.
- **Broadcasting:** Distributes messages to multiple connected clients.
- **Connection Management:** Tracks active connections and handles disconnections.
- **Ping and Pong:** Supports connection health checks.
- **Close Handshake:** Provides a controlled way to close the connection.

## 7. Communication Mechanism

WebSocket uses a persistent TCP connection for bidirectional communication.

- Uses HTTP for the initial handshake.
- Switches protocols through the HTTP Upgrade mechanism.
- Uses `ws://` for standard WebSocket connections.
- Uses `wss://` for secure WebSocket connections.
- Supports text and binary messages.
- Allows continuous communication without repeated HTTP requests.

**Example WebSocket URLs:**

`ws://127.0.0.1:8000/ws/deepu`

`ws://127.0.0.1:8000/ws/rahul`

## 8. Advantages

1. **Real-Time Communication:** Messages can be exchanged immediately between connected clients and servers.
2. **Bidirectional Communication:** Both sides can send and receive messages independently.
3. **Reduced Overhead:** Avoids repeatedly establishing HTTP requests for every message.

## 9. Disadvantages

1. **Connection Management:** Maintaining many active connections requires proper resource management.
2. **Scaling Complexity:** Multiple server instances need a mechanism to coordinate messages between connected clients.
3. **Connection Reliability:** Network interruptions require reconnection handling and message recovery strategies.

## 10. Use Cases

WebSocket is suitable for:

- Real-time chat applications.
- Multiplayer online games.
- Live notifications.
- Collaborative editing applications.
- Live dashboards.
- Real-time trading platforms.
- Location tracking applications.
- Real-time monitoring systems.

---

# Practical Implementation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend framework |
| Uvicorn | ASGI server |
| WebSocket | Communication protocol |
| JSON | Message data format |
| Postman | API testing |

## Project Structure

```text id="wsproj1"
API-EXPLORATION-LAB/
│
└── apps/
    └── websocket_api/
        └── main.py
```

## Implementation Overview

A WebSocket application was implemented using FastAPI.

The implementation demonstrates real-time communication between multiple connected clients.

**WebSocket endpoint:**

`/ws/{client_id}`

**Main components:**

| Component | Purpose |
|---|---|
| ConnectionManager | Manages active WebSocket connections. |
| connect() | Accepts and registers a client connection. |
| disconnect() | Removes a disconnected client. |
| broadcast() | Sends messages to connected clients. |
| receive_json() | Receives JSON messages from a client. |
| send_json() | Sends JSON messages to a client. |

The implementation supports client connections, message exchange, broadcasting, and disconnection handling.

## Testing

The WebSocket implementation was tested using Postman.

**Testing covered:**

- Connecting the first client.
- Connecting multiple clients.
- Sending messages between clients.
- Broadcasting messages to connected clients.
- Testing invalid messages.
- Disconnecting clients.
- Verifying connection management.

**Example client connections:**

Client 1: `ws://127.0.0.1:8000/ws/deepu`

Client 2: `ws://127.0.0.1:8000/ws/rahul`

## Key Takeaways

- WebSocket provides bidirectional communication.
- It establishes a persistent connection using an HTTP handshake.
- Both client and server can send messages independently.
- Connection managers help manage multiple active clients.
- WebSocket is useful for applications requiring continuous real-time communication.