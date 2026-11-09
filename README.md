# 🚀 API Exploration Lab

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/GraphQL-API-E10098?style=for-the-badge&logo=graphql&logoColor=white" alt="GraphQL">
  <img src="https://img.shields.io/badge/gRPC-API-244C5A?style=for-the-badge&logo=google&logoColor=white" alt="gRPC">
  <img src="https://img.shields.io/badge/WebSocket-Real--Time-010101?style=for-the-badge&logo=socketdotio&logoColor=white" alt="WebSocket">
  <img src="https://img.shields.io/badge/Postman-API_Testing-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman">
</p>

<p align="center">
  <b>A comprehensive API exploration project covering 10 API technologies through practical implementations and conceptual studies, focusing on their fundamentals, features, communication mechanisms, and real-world applications.</b>
</p>

---

## 📌 About the Project

API Exploration Lab is a learning project developed to explore and understand different API technologies, their capabilities, communication mechanisms, and practical applications.

The project covers **10 API technologies**, organized into two categories:

- **5 Practical Implementations:** Building and testing APIs using Python and related technologies.
- **5 Conceptual Studies:** Understanding API protocols, components, internal working, features, and communication mechanisms.

The primary objective is to understand how different API technologies enable communication between applications and where each technology is suitable.

## 🎯 Project Objectives

- Understand different API technologies and communication protocols.
- Explore different API communication mechanisms.
- Implement APIs using Python and FastAPI.
- Understand request-response and real-time communication.
- Learn remote procedure calls and event-driven communication.
- Explore XML, JSON, and Protocol Buffers.
- Understand streaming and Publish-Subscribe messaging.
- Test practical API implementations using Postman.
- Study the advantages, disadvantages, and use cases of each technology.
- Maintain structured technical documentation for all 10 technologies.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend programming |
| FastAPI | Backend framework |
| Uvicorn | ASGI server |
| Strawberry GraphQL | GraphQL implementation |
| gRPC | Remote procedure call framework |
| Protocol Buffers | Message definitions and serialization |
| HTTP / HTTP/2 | Communication protocols |
| WebSocket | Bidirectional communication |
| SSE | Server-to-client event streaming |
| JSON | Data exchange format |
| XML | Structured data representation |
| Postman | API testing |
| Git and GitHub | Version control |
| VS Code | Development environment |

---

## ⚡ API Technologies Covered

The project explores 10 technologies divided into practical and conceptual categories.

### 1. Practical Implementations

These five technologies were implemented using Python and tested to understand their actual communication mechanisms.

| No. | API Technology | Key Concepts Covered | Status |
|---:|---|---|---|
| 1 | GraphQL API | Schema, Types, Queries, Mutations, Resolvers, CRUD Operations | Completed |
| 2 | WebSocket API | Handshake, Persistent Connections, Message Exchange, Broadcasting | Completed |
| 3 | gRPC API | Protocol Buffers, Service Definitions, Stubs, Servicers, Unary RPC, CRUD | Completed |
| 4 | Webhooks | Event Triggers, HTTP POST, Payload Handling, Event Processing | Completed |
| 5 | Server-Sent Events (SSE) | EventSource, Event Streams, Heartbeats, Reconnection, Event IDs | Completed |

### 2. Conceptual Studies

These five technologies were studied theoretically, focusing on their components, internal working, communication mechanisms, features, advantages, disadvantages, and use cases.

| No. | Technology | Key Concepts Covered | Status |
|---:|---|---|---|
| 1 | SOAP | XML Messaging, Envelope, Header, Body, WSDL, WS-Security | Completed |
| 2 | XML-RPC | Remote Procedure Calls, XML Messages, Parameters, Fault Handling | Completed |
| 3 | OData | Entity Data Model, Metadata, CRUD, Query Options, Filtering | Completed |
| 4 | MQTT | Publish-Subscribe, Broker, Topics, QoS, Retained Messages, LWT | Completed |
| 5 | WebTransport | HTTP/3, QUIC, Bidirectional Streams, Unidirectional Streams, Datagrams | Completed |

---

## 🔄 Communication Mechanisms Explored

Different API technologies use different communication models.

| Communication Model | Technologies |
|---|---|
| Request-Response | GraphQL, SOAP, XML-RPC, OData |
| Bidirectional Communication | WebSocket, WebTransport |
| Remote Procedure Calls | gRPC, XML-RPC |
| Event-Driven Communication | Webhooks |
| Server-to-Client Streaming | SSE |
| Publish-Subscribe Messaging | MQTT |
| Stream-Based Communication | gRPC, WebTransport |

---

## ⚙️ Practical Features Implemented

| API | Implemented Features |
|---|---|
| GraphQL | User Management, Queries, Mutations, Resolvers, CRUD Operations |
| WebSocket | Multiple Client Connections, Message Exchange, Broadcasting, Disconnection Handling |
| gRPC | User Management, Protocol Buffer Definitions, Client Stub, Server Implementation, CRUD Operations |
| Webhooks | Payment Event Receiver, Success and Failure Event Processing, Unknown Event Handling |
| SSE | Persistent Event Streaming, Server-Generated Events, Heartbeats, Reconnection Concepts |

**Implementation Note:**

The practical implementations use lightweight examples and in-memory storage. They are designed for learning and testing API communication rather than providing complete production systems.

---

## 🌐 API Endpoints and Communication

The practical applications use different communication mechanisms.

| API | Endpoint / Address | Communication |
|---|---|---|
| GraphQL | `/graphql` | HTTP |
| WebSocket | `/ws/{client_id}` | WebSocket |
| gRPC | `localhost:50051` | HTTP/2 |
| Webhooks | `POST /webhooks/payment` | HTTP POST |
| SSE | Configured SSE endpoint | HTTP Event Stream |

### Communication Details

**GraphQL**
- Uses a single endpoint.
- Supports queries and mutations.
- Returns requested data in JSON format.

**WebSocket**
- Maintains persistent connections.
- Supports two-way communication.
- Allows broadcasting messages to connected clients.

**gRPC**
- Uses Protocol Buffers for message definitions.
- Uses generated client stubs and server interfaces.
- Supports remote procedure calls.

**Webhooks**
- Receives event notifications through HTTP POST.
- Processes incoming event payloads.
- Supports event-driven communication.

**SSE**
- Maintains a persistent HTTP connection.
- Sends continuous server-generated events.
- Supports automatic client reconnection through EventSource.

---

## 🧪 Testing with Postman

The practical implementations were tested using Postman to understand their communication behavior and verify their functionality.

### GraphQL Testing

- Retrieve all users.
- Retrieve a user by ID.
- Create a user.
- Update user details.
- Delete a user.

### WebSocket Testing

- Establish multiple client connections.
- Exchange messages between clients.
- Broadcast messages.
- Test invalid messages and disconnection handling.

### gRPC Testing

- Create a user.
- Retrieve a user by ID.
- List all users.
- Update user details.
- Delete a user.

### Webhook Testing

- Send successful payment events.
- Send failed payment events.
- Send unknown event types.
- Verify event-processing responses.

*Postman was used to simulate a webhook provider. No actual payment provider generated these test events.*

### SSE Testing

- Establish an SSE connection.
- Receive server-generated events.
- Understand heartbeat messages.
- Observe reconnection behavior.
- Understand event IDs and Last-Event-ID.

---

## 📁 Project Structure

```text
API-EXPLORATION-LAB/
│
├── apps/
│   │
│   ├── graphql_api/
│   │   └── main.py
│   │
│   ├── websocket_api/
│   │   └── main.py
│   │
│   ├── grpc_api/
│   │   ├── proto/
│   │   │   └── user.proto
│   │   ├── user_pb2.py
│   │   ├── user_pb2_grpc.py
│   │   ├── server.py
│   │   └── client.py
│   │
│   ├── webhook_api/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   └── webhook_routes.py
│   │   └── services/
│   │       └── event_service.py
│   │
│   └── sse_api/
│
├── documentation/
│   │
│   ├── practical/
│   │   ├── graphql/
│   │   │   └── GRAPHQL.md
│   │   ├── websocket/
│   │   │   └── WEBSOCKET.md
│   │   ├── grpc/
│   │   │   └── GRPC.md
│   │   ├── webhooks/
│   │   │   └── WEBHOOKS.md
│   │   └── sse/
│   │       └── SSE.md
│   │
│   └── conceptual/
│       ├── soap/
│       │   └── SOAP.md
│       ├── xml_rpc/
│       │   └── XML_RPC.md
│       ├── odata/
│       │   └── ODATA.md
│       ├── mqtt/
│       │   └── MQTT.md
│       └── webtransport/
│           └── WEBTRANSPORT.md
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📚 Documentation

Each API technology has a dedicated Markdown document containing its important concepts and explanations.

### Practical API Documentation

| Documentation | Description |
|---|---|
| [GraphQL](documentation/practical/graphql/GRAPHQL.md) | Schema, Queries, Mutations, Resolvers, Features, and Implementation |
| [WebSocket](documentation/practical/websocket/WEBSOCKET.md) | Handshake, Connections, Message Exchange, and Broadcasting |
| [gRPC](documentation/practical/grpc/GRPC.md) | Protocol Buffers, Remote Procedure Calls, Stubs, and Services |
| [Webhooks](documentation/practical/webhooks/WEBHOOKS.md) | Event-Driven Communication, Payloads, and Event Processing |
| [SSE](documentation/practical/sse/SSE.md) | Event Streams, EventSource, Heartbeats, and Reconnection |

### Conceptual API Documentation

| Documentation | Description |
|---|---|
| [SOAP](documentation/conceptual/soap/SOAP.md) | XML Messaging, WSDL, SOAP Components, and Communication |
| [XML-RPC](documentation/conceptual/xml_rpc/XML_RPC.md) | Remote Method Invocation, XML Messages, and Fault Handling |
| [OData](documentation/conceptual/odata/ODATA.md) | Entity Data Model, Metadata, Query Options, and CRUD |
| [MQTT](documentation/conceptual/mqtt/MQTT.md) | Broker, Publisher, Subscriber, Topics, and QoS |
| [WebTransport](documentation/conceptual/webtransport/WEBTRANSPORT.md) | HTTP/3, QUIC, Streams, and Datagrams |

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd API-EXPLORATION-LAB
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a local `.env` file using `.env.example` as a reference.

Configure the required values according to the environment variables used by your applications.

**Important:** Never commit `.env` or expose secret credentials on GitHub.

### 5. Run Individual Applications

Each practical API is maintained independently.

**GraphQL:**

```bash
python -m uvicorn apps.graphql_api.main:app --reload
```

**WebSocket:**

```bash
python -m uvicorn apps.websocket_api.main:app --reload
```

Start the other applications using their respective server entry points and configurations.

---

## 🎓 Learning Outcomes

Through this project, the following concepts were explored:

- API fundamentals and communication protocols.
- Different API technologies and their capabilities.
- Request-response communication.
- Bidirectional real-time communication.
- Remote procedure calls.
- XML and JSON data exchange.
- Protocol Buffers and binary serialization.
- Event-driven communication.
- Publish-Subscribe messaging.
- Server-Sent Events and persistent connections.
- HTTP, HTTP/2, HTTP/3, TCP, UDP, and QUIC fundamentals.
- Streaming and message delivery mechanisms.
- API testing using Postman.
- Technical documentation using Markdown.

---

## 🚧 Project Scope and Limitations

This project focuses on understanding different API technologies through practical implementations and conceptual studies.

**Practical implementations:**
- Lightweight demonstration applications.
- In-memory storage for sample data.
- Manual testing using Postman.
- No complete production authentication or database infrastructure.

**Conceptual studies:**
- Theory-based documentation.
- Component and feature explanations.
- Internal communication mechanisms.
- Advantages, disadvantages, and use cases.
- No practical code implementations.

These limitations keep the project focused on API fundamentals and communication concepts.

---

## 🧠 Key Takeaway

> API Exploration Lab provides a structured learning experience covering 10 API technologies through practical implementation and conceptual understanding, helping explore how different applications communicate, exchange information, and interact across networks.