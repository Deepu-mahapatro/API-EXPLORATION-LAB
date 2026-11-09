# WebTransport API

## 1. Overview

WebTransport is a web communication technology that enables low-latency, bidirectional data exchange between clients and servers.

It uses HTTP/3 and the QUIC transport protocol to provide efficient communication over the network.

Unlike traditional HTTP request-response communication, WebTransport supports multiple communication patterns, including bidirectional streams, unidirectional streams, and unreliable datagrams.

It is designed for applications that require real-time communication, low latency, and flexible data transfer.

**Why was WebTransport introduced?**

Traditional HTTP communication is primarily based on request-response interactions.

WebSocket provides bidirectional communication but does not offer the same combination of independent streams and unreliable datagrams.

WebTransport was introduced to provide more flexible communication capabilities using modern transport technologies such as QUIC and HTTP/3.

## 2. Purpose

WebTransport is designed to provide efficient and flexible communication between web clients and servers.

Its main purposes are:

- Enable low-latency communication.
- Support bidirectional data exchange.
- Transfer multiple independent streams of data.
- Support unreliable datagram communication.
- Reduce communication delays caused by transport-level blocking.
- Support real-time web applications.

**Example:**

Consider an online multiplayer game.

The game needs to exchange player movements, positions, and other updates continuously.

WebTransport can use reliable streams for important game information and datagrams for frequent position updates where occasional packet loss is acceptable.

## 3. Core Components

WebTransport contains several important components.

### 3.1 WebTransport Client

The Client is the application that initiates communication with a WebTransport server.

It establishes a session and exchanges data using streams and datagrams.

**Purpose:**
- Initiates WebTransport sessions.
- Sends and receives data.
- Creates communication streams.
- Sends and receives datagrams.

### 3.2 WebTransport Server

The Server accepts WebTransport sessions and handles communication with connected clients.

It manages streams, datagrams, and session-related operations.

**Purpose:**
- Accepts client connections.
- Establishes WebTransport sessions.
- Handles incoming streams.
- Processes datagrams.
- Sends responses and updates.

### 3.3 WebTransport Session

A Session represents an established communication relationship between a client and server.

A session can contain multiple streams and datagrams.

**Purpose:**
- Maintains the communication context.
- Supports multiple data-transfer operations.
- Manages session establishment and closure.

### 3.4 QUIC Protocol

QUIC is a modern transport protocol that operates over UDP.

WebTransport uses QUIC through HTTP/3 to provide low-latency communication.

**Purpose:**
- Provides reliable transport for streams.
- Supports multiple independent streams.
- Provides connection security.
- Supports low-latency communication.

### 3.5 HTTP/3

HTTP/3 is the latest major version of HTTP and uses QUIC as its transport protocol.

WebTransport uses HTTP/3 mechanisms to establish and manage communication sessions.

### 3.6 Bidirectional Streams

Bidirectional streams allow both the client and server to send and receive data independently through the same stream.

They provide reliable and ordered data delivery.

### 3.7 Unidirectional Streams

Unidirectional streams allow data to flow in only one direction.

The stream initiator sends data, and the receiving side reads it.

### 3.8 Datagrams

Datagrams allow applications to exchange messages without requiring reliable delivery or guaranteed ordering.

They are useful when low latency is more important than receiving every message.

### 3.9 Stream Management

Stream management handles the creation, reading, writing, and closing of communication streams.

### 3.10 Session Management

Session management handles the establishment, lifecycle, and closure of WebTransport sessions.

## 4. Architecture

WebTransport follows a client-server architecture based on HTTP/3 and QUIC.

### WebTransport Architecture Diagram

```text id="wtflow1"
           Web Client
               |
               |
        WebTransport API
               |
               v
       HTTP/3 Communication
               |
               v
          QUIC Protocol
               |
       +-------+--------+
       |                |
       v                v
 Reliable Streams    Datagrams
       |                |
       +-------+--------+
               |
               v
       WebTransport Server
               |
               v
       Server Application
```

### Architecture Components

**1. Web Client**

Initiates the WebTransport session and exchanges data with the server.

**2. WebTransport API**

Provides the client-side interface for establishing sessions and managing streams and datagrams.

**3. HTTP/3**

Handles the HTTP-based session establishment and communication mechanisms.

**4. QUIC**

Provides the underlying transport capabilities, including independent streams and secure communication.

**5. Reliable Streams**

Transfer data with reliability and ordering guarantees within each stream.

**6. Datagrams**

Transfer messages without guaranteed delivery or ordering.

**7. WebTransport Server**

Receives client communication and processes the transferred data.

## 5. Internal Working

WebTransport communication works through the following steps.

### Step 1: Session Initiation

The client initiates a WebTransport session by specifying the server endpoint.

### Step 2: Connection Establishment

The client and server establish communication using HTTP/3 over QUIC.

### Step 3: Session Acceptance

The server processes the session request and accepts the WebTransport session when the connection and request are valid.

### Step 4: Stream Creation

The client or server can create communication streams depending on the required communication pattern.

### Step 5: Data Transmission

The applications exchange data through reliable bidirectional streams, unidirectional streams, or datagrams.

### Step 6: Data Processing

The receiving application processes the transferred data according to the application requirements.

### Step 7: Stream Management

Individual streams can be completed or closed independently without necessarily closing the entire session.

### Step 8: Session Closure

The client or server can close the WebTransport session when communication is no longer required.

**Complete communication flow:**

```text id="wtflow2"
Client
  |
  | 1. Initiate Session
  |
  v
HTTP/3 over QUIC
  |
  | 2. Establish Connection
  |
  v
WebTransport Server
  |
  | 3. Accept Session
  |
  v
Communication Session
  |
  +----------------------+
  |                      |
  v                      v
Reliable Streams      Datagrams
  |                      |
  v                      v
Ordered Data          Low-Latency Data
  |                      |
  +----------+-----------+
             |
             v
       Data Processing
             |
             v
       Session Closure
```

## 6. Functions and Features

WebTransport provides several important communication features.

### 6.1 Bidirectional Streams

Bidirectional streams allow both sides to send and receive data through the same stream.

**Features:**
- Supports two-way communication.
- Provides reliable delivery.
- Maintains ordering within each stream.
- Suitable for important application data.

### 6.2 Unidirectional Streams

Unidirectional streams allow data to travel in one direction.

**Features:**
- Supports one-way data transfer.
- Provides reliable delivery.
- Maintains ordering within the stream.
- Useful when only one side needs to send data.

### 6.3 Datagrams

Datagrams support low-latency message exchange without reliable delivery guarantees.

**Features:**
- Does not guarantee delivery.
- Does not guarantee ordering.
- Avoids waiting for retransmission of lost datagrams.
- Suitable for time-sensitive information.

### 6.4 Multiple Independent Streams

WebTransport supports multiple streams within one session.

Each stream operates independently at the QUIC transport level.

This reduces transport-level head-of-line blocking between independent streams.

### 6.5 Low-Latency Communication

WebTransport uses QUIC to provide efficient communication and reduce connection-related delays.

### 6.6 Secure Communication

WebTransport uses secure QUIC connections, which provide encryption and authentication through TLS 1.3.

### 6.7 Session Management

WebTransport supports the creation, maintenance, and closure of communication sessions.

### 6.8 Flow Control

QUIC provides flow-control mechanisms that help manage how much data is transferred through connections and individual streams.

### 6.9 Congestion Control

QUIC includes congestion-control mechanisms that help manage network traffic and avoid overwhelming the network.

### 6.10 Stream Prioritization and Scheduling

Applications and implementations can manage how different streams are scheduled and processed.

The exact scheduling behavior depends on the implementation and application design.

## 7. Communication Mechanism

WebTransport uses HTTP/3 and QUIC for communication.

### 7.1 HTTP/3

HTTP/3 provides the HTTP-based mechanism used to establish WebTransport sessions.

It operates over QUIC instead of TCP.

### 7.2 QUIC

QUIC is the transport protocol responsible for reliable streams, datagrams, connection security, and transport-level communication.

It operates over UDP.

### 7.3 Communication Types

WebTransport supports three main data-transfer mechanisms.

| Communication Type | Direction | Reliability | Ordering |
|---|---|---|---|
| Bidirectional Stream | Two-way | Reliable | Ordered within the stream |
| Unidirectional Stream | One-way | Reliable | Ordered within the stream |
| Datagram | Two-way communication is possible | Unreliable | Not guaranteed |

### 7.4 Communication Process

1. Client initiates a WebTransport session.
2. HTTP/3 establishes the session over QUIC.
3. Server accepts the session.
4. Client and server create streams when required.
5. Applications exchange reliable data through streams.
6. Applications exchange time-sensitive data through datagrams.
7. Streams and sessions are closed when communication finishes.

### 7.5 Transport Protocol Stack

```text id="wtstack1"
       Application Layer
         WebTransport
               |
               v
          HTTP/3 Layer
               |
               v
           QUIC Layer
               |
               v
            UDP Layer
               |
               v
          IP Network
```

Each layer has a different responsibility:

- WebTransport manages application communication sessions.
- HTTP/3 provides the HTTP-based session mechanism.
- QUIC handles secure transport and streams.
- UDP carries QUIC packets across the network.
- IP provides network-level packet delivery.

## 8. Advantages

1. **Low Latency:** QUIC provides efficient connection establishment and communication, making WebTransport suitable for time-sensitive applications.

2. **Flexible Communication:** Supports bidirectional streams, unidirectional streams, and unreliable datagrams within the same session.

3. **Independent Streams:** Multiple streams can operate independently, reducing transport-level head-of-line blocking between streams.

## 9. Disadvantages

1. **Implementation Complexity:** WebTransport requires understanding HTTP/3, QUIC, streams, datagrams, and session management.

2. **Limited Compatibility:** Browser, server, and network support may vary, so compatibility must be considered.

3. **Infrastructure Requirements:** Requires HTTP/3 and QUIC-capable infrastructure, which may be more difficult to configure than traditional HTTP or WebSocket systems.

## 10. Use Cases

WebTransport is suitable for applications requiring low latency and flexible data transfer.

### 10.1 Multiplayer Online Games

Used for transferring player positions, movements, and game updates with low latency.

### 10.2 Real-Time Communication

Supports applications that exchange continuous data between clients and servers.

### 10.3 Live Streaming Applications

Can support low-latency data delivery and interactive streaming workflows.

### 10.4 Collaborative Applications

Useful for exchanging real-time updates between users working on shared resources.

### 10.5 Virtual Reality and Augmented Reality

Can support time-sensitive communication for interactive VR and AR applications.

### 10.6 Remote Control Systems

Useful for transferring commands and receiving updates from remotely controlled systems.

### 10.7 Interactive Data Applications

Supports applications that require multiple independent data streams and fast message delivery.

---

## Key Takeaways

- WebTransport is a modern web communication technology built on HTTP/3 and QUIC.
- It supports bidirectional streams, unidirectional streams, and datagrams.
- Reliable streams provide ordered data delivery.
- Datagrams provide low-latency communication without guaranteed delivery.
- Multiple independent streams reduce transport-level head-of-line blocking.
- QUIC operates over UDP and provides secure communication using TLS 1.3.
- WebTransport is suitable for real-time applications requiring flexible and low-latency data transfer.