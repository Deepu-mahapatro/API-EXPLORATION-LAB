# gRPC API

## 1. Overview

gRPC (Google Remote Procedure Call) is a high-performance, open-source communication framework developed by Google.

It allows applications to communicate with each other by calling methods on a remote server as if they were local functions.

gRPC uses Protocol Buffers (Protobuf) as its interface definition language and commonly uses HTTP/2 for communication.

## 2. Purpose

gRPC is designed to enable fast and efficient communication between distributed applications and services.

Its main purposes are:

- Enable communication between different services.
- Reduce communication overhead.
- Support high-performance data exchange.
- Provide strongly typed service contracts.
- Support multiple programming languages.

## 3. Core Components

| Component | Description |
|---|---|
| Protocol Buffers | Defines the structure of messages and services. |
| `.proto` File | Contains service definitions and message structures. |
| gRPC Server | Receives requests and executes service methods. |
| gRPC Client | Sends requests to the remote server. |
| Stub | Client-side object used to call remote methods. |
| Servicer | Implements the server-side service methods. |
| Channel | Establishes communication between the client and server. |
| Serialization | Converts structured messages into a transferable binary format. |

## 4. Architecture

gRPC follows a client-server communication architecture.

```text
          gRPC Client
               |
               v
          Client Stub
               |
               v
        HTTP/2 Connection
               |
               v
          gRPC Server
               |
               v
       Service Implementation
               |
               v
          Data Source
               |
               v
        Response to Client
```

**Main flow:**

1. The client calls a method using the generated stub.
2. The request is serialized using Protocol Buffers.
3. The request travels through an HTTP/2 connection.
4. The server receives and deserializes the request.
5. The corresponding service method executes.
6. The server sends the serialized response back to the client.

## 5. Internal Working

gRPC works through the following steps:

1. **Service Definition:** Services and message structures are defined in a `.proto` file.
2. **Code Generation:** The Protocol Buffers compiler generates client and server code.
3. **Server Setup:** The server implements the generated service interface.
4. **Client Setup:** The client creates a channel and uses the generated stub.
5. **Request:** The client invokes a remote method through the stub.
6. **Serialization:** The request is converted into binary Protobuf data.
7. **Communication:** HTTP/2 transfers the request to the server.
8. **Execution:** The server processes the request and executes the method.
9. **Response:** The server returns the result to the client.

## 6. Functions and Features

**Important gRPC functions and features:**

- **Remote Procedure Calls:** Call methods on remote services.
- **Protocol Buffers:** Efficient binary message serialization.
- **Code Generation:** Automatically generates client and server code.
- **Unary RPC:** One request followed by one response.
- **Server Streaming:** One request followed by multiple responses.
- **Client Streaming:** Multiple requests followed by one response.
- **Bidirectional Streaming:** Both client and server exchange multiple messages.
- **HTTP/2:** Supports multiplexing and efficient communication.
- **Deadline and Timeout:** Controls how long a client waits for a response.
- **Status Codes:** Communicates the result or failure of an RPC operation.

*Note: The practical implementation in this project focuses on unary RPC operations.*

## 7. Communication Mechanism

gRPC commonly uses HTTP/2 and Protocol Buffers for communication.

- HTTP/2 handles the transport and communication.
- Protocol Buffers define and serialize messages.
- The client uses a generated stub to invoke remote methods.
- The server executes the requested service method.
- The server returns a structured response.

**Default gRPC port used in this project:**

`50051`

## 8. Advantages

1. **High Performance:** Binary serialization and HTTP/2 provide efficient communication.
2. **Strongly Typed Contracts:** Protobuf defines structured messages and service methods.
3. **Multi-language Support:** Services can communicate across different programming languages.

## 9. Disadvantages

1. **Complex Setup:** Requires service definitions and generated code.
2. **Browser Compatibility:** Direct browser support is limited compared with traditional HTTP APIs.
3. **Debugging Complexity:** Binary Protobuf messages are less human-readable than JSON.

## 10. Use Cases

gRPC is suitable for:

- Microservices communication.
- Distributed systems.
- Internal backend service communication.
- High-performance applications.
- Real-time streaming applications.
- Communication between services written in different programming languages.

---

# Practical Implementation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| gRPC | Remote procedure call framework |
| Protocol Buffers | Service and message definitions |
| grpcio | Python gRPC runtime |
| grpcio-tools | Protocol Buffer code generation |
| Postman | API testing |

## Project Structure

```text
API-EXPLORATION-LAB/
│
└── apps/
    └── grpc_api/
        ├── proto/
        │   └── user.proto
        │
        ├── user_pb2.py
        ├── user_pb2_grpc.py
        ├── server.py
        └── client.py
```

## Implementation Overview

The gRPC API was implemented using Python and Protocol Buffers.

A simple **User Management System** was selected to understand remote procedure calls.

The implementation includes:

| Operation | Purpose |
|---|---|
| CreateUser | Create a new user |
| GetUser | Retrieve a user by ID |
| ListUsers | Retrieve all users |
| UpdateUser | Update existing user details |
| DeleteUser | Delete a user |

The `.proto` file defines the service and message structures.

Generated Python files provide the required client stubs, server interfaces, and message classes.

The implementation uses in-memory storage with a lock for thread-safe access. Data is not permanently stored in a database.

## Testing

The gRPC API was tested using Postman.

**Testing covered:**

- Creating a user.
- Retrieving a user by ID.
- Retrieving all users.
- Updating user details.
- Deleting a user.
- Checking server responses and error handling.

**Server address:**

`localhost:50051`

## Key Takeaways

- gRPC enables communication through remote procedure calls.
- Protocol Buffers define service contracts and message structures.
- HTTP/2 handles the communication between client and server.
- Generated stubs simplify client-side method calls.
- gRPC supports unary and streaming communication patterns.