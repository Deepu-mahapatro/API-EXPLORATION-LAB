# MQTT (Message Queuing Telemetry Transport)

## 1. Overview

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for communication between devices over networks with limited bandwidth, high latency, or unreliable connectivity.

It follows a **Publish-Subscribe (Pub/Sub)** messaging model, where devices communicate through a central component called a Broker.

MQTT is widely used in IoT (Internet of Things) applications because it requires low network bandwidth and has minimal communication overhead.

**Why was MQTT introduced?**

Traditional communication protocols can create unnecessary network overhead for small devices with limited processing power and memory.

MQTT was designed to provide lightweight, efficient, and reliable message exchange between connected devices.

## 2. Purpose

MQTT is designed to enable efficient communication between connected devices and applications.

Its main purposes are:

- Enable lightweight messaging between devices.
- Support communication in low-bandwidth networks.
- Reduce network communication overhead.
- Support unreliable or intermittent network connections.
- Enable real-time message distribution.
- Connect large numbers of IoT devices.

**Example:**

Consider a smart home with temperature sensors and an air conditioning system.

The temperature sensor publishes temperature data to an MQTT Broker. The air conditioning system subscribes to the relevant topic and receives updates whenever new temperature data is published.

## 3. Core Components

MQTT communication involves several important components.

### 3.1 MQTT Client

An MQTT Client is any device or application that connects to an MQTT Broker.

A client can publish messages, subscribe to topics, or perform both operations.

**Examples:**
- Temperature sensors.
- Smart home devices.
- Mobile applications.
- IoT gateways.
- Monitoring applications.

### 3.2 MQTT Broker

The Broker is the central component responsible for receiving, filtering, and distributing messages between connected clients.

It receives published messages and forwards them to clients subscribed to the corresponding topics.

**Purpose:**
- Accept client connections.
- Receive published messages.
- Manage subscriptions.
- Distribute messages to subscribers.
- Manage connection-related operations.

### 3.3 Publisher

A Publisher is an MQTT client that sends messages to the Broker.

It publishes data under a particular topic.

**Example:**

A temperature sensor publishes the current temperature under:

`home/room1/temperature`

### 3.4 Subscriber

A Subscriber is an MQTT client that receives messages from the Broker.

It subscribes to one or more topics to receive relevant updates.

**Example:**

A mobile application subscribes to:

`home/room1/temperature`

It receives temperature updates published under that topic.

### 3.5 Topic

A Topic is a named communication channel used to organize and identify messages.

Publishers send messages to topics, and subscribers receive messages by subscribing to those topics.

**Example topics:**

- `home/temperature`
- `home/livingroom/light`
- `factory/machine1/status`
- `vehicle/location`

Topics support hierarchical structures using `/` separators and can support wildcards in subscriptions.

### 3.6 Message

A Message is the actual data transferred between MQTT clients through the Broker.

It generally contains a payload and is associated with a topic and delivery options.

**Example:**

A temperature sensor sends:

`{"temperature": 28}`

### 3.7 Subscription

A Subscription represents a client's interest in receiving messages from a particular topic or topic pattern.

The Broker uses subscription information to determine where published messages should be delivered.

### 3.8 Quality of Service (QoS)

QoS defines the message delivery guarantee used by MQTT.

It provides three delivery levels:

- QoS 0 – At most once.
- QoS 1 – At least once.
- QoS 2 – Exactly once.

These levels determine how much acknowledgement and retransmission are involved in message delivery.

## 4. Architecture

MQTT follows a Publish-Subscribe architecture with a central Broker.

### MQTT Architecture Diagram

```text
       Publisher 1              Publisher 2
            |                        |
            | Publish Message        |
            v                        v
       +--------------------------------+
       |                                |
       |          MQTT Broker           |
       |                                |
       |     Topic Management           |
       |     Message Distribution       |
       |     Client Management          |
       |                                |
       +--------------------------------+
            |                        |
            | Subscribe              |
            v                        v
       Subscriber 1             Subscriber 2
```

### Architecture Components

**1. Publisher**

Generates information and sends messages to the MQTT Broker.

**2. MQTT Broker**

Receives messages and manages topic-based message distribution.

**3. Topic**

Identifies the category or channel associated with a message.

**4. Subscriber**

Receives messages from the Broker based on its subscriptions.

**5. Message**

Contains the actual information transferred between applications.

### Important Architecture Concept

Publishers and subscribers do not need to communicate directly.

The Broker handles message distribution between them.

This means publishers do not need to know which clients are receiving their messages.

## 5. Internal Working

MQTT communication works through the following steps.

### Step 1: Client Connection

The MQTT client establishes a connection with the Broker using an MQTT-supported transport.

### Step 2: Connection Establishment

The client sends a CONNECT packet to the Broker.

The Broker processes the connection request and returns a CONNACK packet indicating whether the connection was accepted.

### Step 3: Topic Subscription

A subscriber sends a SUBSCRIBE packet to register its interest in a particular topic.

The Broker processes the subscription and acknowledges it with a SUBACK packet.

### Step 4: Message Publishing

A publisher sends a PUBLISH packet containing the topic and message payload.

### Step 5: Message Reception

The Broker receives the published message and checks its subscription information.

### Step 6: Message Distribution

The Broker forwards the message to clients subscribed to the matching topic.

### Step 7: Message Delivery

The subscriber receives the published message.

Depending on the selected QoS level, additional acknowledgement and retransmission mechanisms may be involved.

### Step 8: Disconnection

When a client wants to disconnect, it sends a DISCONNECT packet to the Broker.

**Complete communication flow:**

```text
Publisher
    |
    | CONNECT
    v
MQTT Broker
    |
    | CONNACK
    v
Publisher Connected

Subscriber
    |
    | SUBSCRIBE
    v
MQTT Broker
    |
    | SUBACK
    v
Subscriber Registered

Publisher
    |
    | PUBLISH
    v
MQTT Broker
    |
    | Topic Matching
    v
Subscriber
    |
    | Receives Message
    v
Message Delivered
```

## 6. Functions and Features

MQTT provides several important communication mechanisms and features.

### 6.1 Publish-Subscribe Model

MQTT uses a Publish-Subscribe model instead of direct request-response communication.

Publishers send messages to topics, and subscribers receive messages through the Broker.

This separates message producers from message consumers.

### 6.2 Topic-Based Messaging

Topics organize messages into logical categories.

A client can subscribe to a specific topic or use wildcard filters.

MQTT supports two main wildcards:

- **Single-Level Wildcard (+):** Matches one topic level.
- **Multi-Level Wildcard (#):** Matches multiple topic levels and must appear at the end of a topic filter.

For example:

`home/+/temperature`

Can match:

- `home/room1/temperature`
- `home/room2/temperature`

### 6.3 Quality of Service (QoS)

MQTT provides three delivery levels.

| QoS | Delivery Guarantee | Explanation |
|---|---|---|
| QoS 0 | At most once | Message is sent without delivery acknowledgement. |
| QoS 1 | At least once | Message is acknowledged, but duplicates are possible. |
| QoS 2 | Exactly once | Uses a multi-step handshake to ensure exactly-once protocol delivery. |

Higher QoS levels involve additional communication overhead.

### 6.4 Retained Messages

A retained message allows the Broker to store the latest retained message for a topic.

When a new subscriber subscribes to that topic, the Broker can immediately send the stored message.

**Example:**

A temperature sensor publishes the latest temperature as a retained message.

A newly connected monitoring application can receive that latest value without waiting for another sensor update.

### 6.5 Last Will and Testament (LWT)

LWT allows a client to register a message with the Broker when connecting.

If the client disconnects unexpectedly, the Broker can publish that configured message to the specified topic.

**Example:**

A smart device unexpectedly loses its connection.

The Broker publishes:

`device/status = offline`

This helps other applications identify the device's connection status.

### 6.6 Persistent Sessions

MQTT supports session persistence.

Depending on the protocol version and session settings, the Broker can retain session information such as subscriptions and eligible queued messages when a client disconnects.

This helps clients resume communication after reconnecting.

### 6.7 Keep Alive

Keep Alive is a connection-maintenance mechanism.

It allows the Broker to detect clients that are no longer communicating.

MQTT uses PINGREQ and PINGRESP packets to check whether the connection is still active when necessary.

### 6.8 Wildcard Subscriptions

MQTT allows subscribers to subscribe to multiple related topics using wildcard characters.

This reduces the need to create separate subscriptions for every individual topic.

### 6.9 Authentication and Security

MQTT supports client authentication and can use TLS to protect communication.

Additional authorization mechanisms can control which topics clients are allowed to publish or subscribe to.

### 6.10 Will Delay

MQTT 5.0 supports Will Delay, which allows the Broker to delay publishing a client's Will Message after an unexpected disconnection.

This can help avoid unnecessary offline notifications during temporary network interruptions.

## 7. Communication Mechanism

MQTT uses a lightweight messaging protocol based on the Publish-Subscribe communication model.

### 7.1 Transport Protocols

MQTT commonly operates over:

| Transport | Purpose |
|---|---|
| TCP | Provides reliable transport for MQTT communication. |
| TLS | Secures MQTT communication over TCP. |
| WebSocket | Allows MQTT communication through WebSocket connections. |
| WebSocket over TLS | Provides secure MQTT communication through WebSocket connections. |

### 7.2 MQTT Communication Ports

| Port | Purpose |
|---|---|
| 1883 | Standard MQTT over TCP without TLS. |
| 8883 | MQTT over TLS. |
| 80 | Commonly used for WebSocket connections without TLS. |
| 443 | Commonly used for secure WebSocket connections. |

WebSocket ports depend on the Broker configuration.

### 7.3 MQTT Control Packets

MQTT defines different control packets for communication.

| Packet | Purpose |
|---|---|
| CONNECT | Initiates a client connection. |
| CONNACK | Acknowledges a connection request. |
| PUBLISH | Transfers a message to a topic. |
| SUBSCRIBE | Requests a topic subscription. |
| SUBACK | Acknowledges a subscription request. |
| UNSUBSCRIBE | Removes a topic subscription. |
| UNSUBACK | Acknowledges an unsubscribe request. |
| PINGREQ | Checks connection activity. |
| PINGRESP | Responds to a ping request. |
| DISCONNECT | Indicates an intentional disconnection. |

### 7.4 Communication Process

1. Client establishes a connection with the Broker.
2. Publisher sends a message to a topic.
3. Broker receives the message.
4. Broker identifies matching subscriptions.
5. Broker forwards the message to subscribers.
6. Subscribers receive the message based on the selected QoS and session conditions.

## 8. Advantages

1. **Lightweight Communication:** MQTT has low protocol overhead, making it suitable for devices with limited memory and processing power.

2. **Efficient Message Distribution:** The Publish-Subscribe model allows one publisher to distribute messages to multiple subscribers through a Broker.

3. **Flexible Delivery Guarantees:** QoS levels provide different message delivery guarantees based on application requirements.

## 9. Disadvantages

1. **Broker Dependency:** Communication depends on the MQTT Broker, making Broker availability important.

2. **Limited Built-in Data Structure:** MQTT does not define a standard application-level payload format. Applications must agree on their own message structures.

3. **Security Configuration:** Authentication, authorization, and TLS must be configured properly to protect communication.

## 10. Use Cases

MQTT is widely used in IoT systems and applications that require lightweight communication.

### 10.1 Smart Home Systems

Used for communication between smart lights, temperature sensors, security devices, and home automation applications.

### 10.2 Industrial IoT

Used to collect machine data, monitor industrial equipment, and communicate sensor information.

### 10.3 Smart Agriculture

Used to transfer soil moisture, temperature, humidity, and irrigation sensor data.

### 10.4 Vehicle Monitoring

Used for transmitting vehicle location, status, and sensor information.

### 10.5 Healthcare Monitoring

Used for communication between connected monitoring devices and healthcare applications.

### 10.6 Energy Management

Used in smart meters and energy monitoring systems to exchange consumption and device status information.

### 10.7 Remote Monitoring

Used to monitor connected devices and receive updates from systems located in remote environments.

---

## Key Takeaways

- MQTT is a lightweight messaging protocol designed mainly for IoT communication.
- It follows the Publish-Subscribe communication model.
- The MQTT Broker manages message distribution between clients.
- Topics organize messages and control which subscribers receive them.
- QoS provides three message delivery levels: 0, 1, and 2.
- Retained messages, persistent sessions, and Last Will and Testament support different communication requirements.
- MQTT commonly uses TCP for transport and can also operate over WebSocket.
- It is suitable for low-bandwidth networks and resource-constrained devices.