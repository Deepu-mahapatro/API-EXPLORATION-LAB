# Server-Sent Events (SSE)

## 1. Overview

Server-Sent Events (SSE) is a web technology that allows a server to continuously send updates to a client over a single HTTP connection.

It provides one-way communication, where data flows only from the server to the client.

SSE uses the standard HTTP protocol and sends updates in a text-based event stream format.

## 2. Purpose

SSE is designed to deliver real-time updates from a server without requiring the client to repeatedly request new data.

Its main purposes are:

- Deliver real-time server updates.
- Maintain a persistent HTTP connection.
- Reduce repeated polling requests.
- Automatically reconnect when a connection is interrupted.
- Send continuous updates to browser applications.

## 3. Core Components

| Component | Description |
|---|---|
| SSE Client | Receives continuous updates from the server. |
| SSE Server | Generates and sends event data. |
| EventSource | Browser API used to establish an SSE connection. |
| HTTP Connection | Maintains communication between client and server. |
| Event Stream | Continuous stream of server-generated events. |
| Event ID | Identifies an event and can support reconnection. |
| Retry Field | Specifies the reconnection delay in milliseconds. |
| Heartbeat | Periodic comment sent by the server to help keep idle connections active. |

## 4. Architecture

SSE follows a server-to-client communication architecture.

```text id="sseflow1"
          Client Application
                 |
                 | HTTP GET Request
                 v
           SSE Endpoint
                 |
                 v
          SSE Server Logic
                 |
                 v
          Event Generation
                 |
                 v
          HTTP Event Stream
                 |
                 v
          Client Receives
            Updates
```

**Main flow:**

1. The client establishes an SSE connection using an HTTP GET request.
2. The server accepts the connection.
3. The server sends the event stream using `text/event-stream`.
4. The client continuously receives updates.
5. The connection remains open for future events.
6. If disconnected, the browser can automatically reconnect.

## 5. Internal Working

SSE works through the following steps:

1. **Connection Request:** The client creates an EventSource connection to the SSE endpoint.
2. **HTTP Request:** The browser sends an HTTP GET request.
3. **Connection Establishment:** The server accepts the request and prepares the event stream.
4. **Content Type:** The server responds with `text/event-stream`.
5. **Event Generation:** The server generates updates whenever required.
6. **Data Transmission:** Events are continuously sent through the HTTP connection.
7. **Client Reception:** The browser receives and processes the events.
8. **Reconnection:** If the connection is interrupted, EventSource automatically attempts to reconnect.

The connection does not automatically close just because there are no new events. It can remain open until the client, server, or network closes it.

## 6. Functions and Features

**Important SSE fields and features:**

- **data:** Contains the event data sent to the client.
- **event:** Specifies the event type.
- **id:** Assigns an identifier to an event.
- **retry:** Specifies the reconnection delay in milliseconds.
- **EventSource:** Browser API for receiving SSE updates.
- **Automatic Reconnection:** EventSource attempts to reconnect after an unexpected disconnection.
- **Last-Event-ID:** Allows the browser to communicate the last received event ID during reconnection.
- **Heartbeat:** Server sends periodic comments to help prevent idle connection timeouts.
- **One-Way Communication:** Data flows from server to client.

**Important:** SSE does not automatically store or replay missed events. Event storage and replay must be implemented by the server if required.

## 7. Communication Mechanism

SSE uses HTTP for continuous server-to-client communication.

- Uses HTTP GET to establish the connection.
- Uses the `text/event-stream` content type.
- Sends events in a text-based format.
- Maintains a persistent HTTP connection.
- Supports automatic reconnection through EventSource.
- Uses event IDs and `Last-Event-ID` for optional event recovery.

**Example content type:**

`Content-Type: text/event-stream`

## 8. Advantages

1. **Simple Implementation:** Uses standard HTTP without requiring a separate communication protocol.
2. **Automatic Reconnection:** Browser EventSource handles reconnection after unexpected disconnections.
3. **Efficient Updates:** Avoids repeated polling requests for server-generated updates.

## 9. Disadvantages

1. **One-Way Communication:** The server can send data to the client, but the client cannot send messages through the same SSE stream.
2. **Text-Based Data:** SSE is designed for text-based event streams rather than direct binary message transmission.
3. **Connection Limitations:** Browser and server connection limits can affect applications with many simultaneous connections.

## 10. Use Cases

SSE is suitable for:

- Live notifications.
- Real-time dashboards.
- Live score updates.
- Stock price updates.
- Order status tracking.
- Live monitoring systems.
- Progress updates for long-running tasks.
- Server-generated alerts.

---

# Practical Implementation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend framework |
| Uvicorn | ASGI server |
| HTTP | Communication protocol |
| Postman | API testing |

## Project Structure

The SSE implementation is maintained inside the `sse_api` application.

```text id="sseproj1"
API-EXPLORATION-LAB/
│
└── apps/
    └── sse_api/
        └── main.py
```

## Implementation Overview

A lightweight SSE implementation was developed using FastAPI.

The implementation demonstrates:

- Establishing an SSE connection.
- Sending continuous server-generated events.
- Using the `text/event-stream` response format.
- Maintaining an open HTTP connection.
- Sending heartbeat comments.
- Understanding client reconnection behavior.

The implementation does not require a database, Redis, or Celery.

## Testing

The SSE implementation was tested to understand the event-stream communication mechanism.

**Testing covered:**

- Establishing an SSE connection.
- Receiving server-generated events.
- Observing continuous event delivery.
- Understanding heartbeat messages.
- Understanding automatic reconnection behavior.
- Understanding how event IDs and `Last-Event-ID` can support event recovery.

## Key Takeaways

- SSE provides one-way communication from server to client.
- It uses a persistent HTTP connection.
- EventSource is the browser API used to receive events.
- Automatic reconnection is handled by the browser.
- Event storage and replay require additional server-side implementation.
- Heartbeats help keep idle connections active.