# Webhooks

## 1. Overview

A Webhook is an event-driven communication mechanism that allows one application to automatically send data to another application when a specific event occurs.

It uses HTTP requests to notify another system about events without requiring continuous polling.

For example, when a payment is successful, a payment provider can automatically send a notification to the application's registered webhook endpoint.

## 2. Purpose

Webhooks are designed to enable automatic communication between applications whenever an event occurs.

Their main purposes are:

- Notify applications about important events.
- Enable event-driven communication.
- Avoid repeated polling requests.
- Automatically transfer event data between systems.
- Trigger actions in response to external events.

## 3. Core Components

| Component | Description |
|---|---|
| Event Source | Application or service where an event occurs. |
| Event | An action or activity that triggers a notification. |
| Webhook Provider | System responsible for sending the event notification. |
| Webhook Endpoint | HTTP endpoint that receives the notification. |
| HTTP Request | Carries event information to the receiving application. |
| Payload | Contains event details, usually in JSON format. |
| Event Handler | Processes the received event. |
| Webhook Secret | Used to verify the authenticity of incoming webhook requests. |

## 4. Architecture

Webhooks follow an event-driven communication architecture.

```text id="whflow1"
       Event Source
             |
             v
        Event Occurs
             |
             v
      Webhook Provider
             |
             v
       HTTP POST Request
             |
             v
      Webhook Endpoint
             |
             v
        Event Handler
             |
             v
       Event Processing
             |
             v
        HTTP Response
```

**Main flow:**

1. An event occurs in the provider's application.
2. The provider identifies the registered webhook endpoint.
3. The provider sends an HTTP POST request.
4. The receiving application accepts the request.
5. The event handler processes the payload.
6. The receiving application returns an HTTP response.

## 5. Internal Working

Webhooks work through the following steps:

1. **Endpoint Registration:** The receiving application provides a webhook URL to the provider.
2. **Event Occurrence:** A specific event happens in the provider's system.
3. **Event Detection:** The provider identifies the event and prepares its data.
4. **Request Generation:** The provider creates an HTTP POST request containing the event payload.
5. **Request Delivery:** The provider sends the request to the registered webhook endpoint.
6. **Payload Reception:** The receiving application accepts the incoming request.
7. **Event Processing:** The event handler identifies and processes the event.
8. **Response:** The receiving application returns an HTTP status code to acknowledge the request.

## 6. Functions and Features

**Important webhook functions and features:**

- **Event Triggering:** Initiates notifications when specific events occur.
- **HTTP POST:** Commonly used to deliver webhook notifications.
- **Payload:** Transfers event information, usually in JSON format.
- **Endpoint Registration:** Defines where event notifications should be delivered.
- **Event Filtering:** Allows applications to subscribe to specific event types.
- **Signature Verification:** Helps verify that a request genuinely came from the provider.
- **Retries:** Providers may retry delivery when the receiving endpoint fails.
- **Idempotency:** Helps prevent duplicate event processing.
- **Event Handling:** Executes application logic based on the received event.

## 7. Communication Mechanism

Webhooks commonly use HTTP for application-to-application communication.

- Uses HTTP POST requests.
- Sends event data through request payloads.
- Commonly uses JSON as the data format.
- The provider initiates communication when an event occurs.
- The receiving application responds with an HTTP status code.
- Communication is event-driven rather than continuously requested by the receiver.

**Example endpoint:**

`POST /webhooks/payment`

## 8. Advantages

1. **Automatic Notifications:** Applications receive updates whenever configured events occur.
2. **Reduced Polling:** Eliminates the need for repeated requests to check for updates.
3. **Event-Driven Integration:** Allows different applications to communicate based on events.

## 9. Disadvantages

1. **Delivery Failures:** Network issues or unavailable endpoints can prevent successful event delivery.
2. **Duplicate Events:** Providers may retry requests, resulting in duplicate notifications.
3. **Security Risks:** Incoming requests must be verified to prevent unauthorized or fake events.

## 10. Use Cases

Webhooks are suitable for:

- Payment success and failure notifications.
- Order status updates.
- GitHub repository events.
- CI/CD pipeline notifications.
- User registration notifications.
- Third-party application integrations.
- Messaging and notification systems.
- Subscription and billing updates.

---

# Practical Implementation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend framework |
| Uvicorn | ASGI server |
| HTTP | Communication protocol |
| JSON | Event payload format |
| Postman | API testing |

## Project Structure

```text id="whproj1"
API-EXPLORATION-LAB/
│
└── apps/
    └── webhook_api/
        ├── main.py
        │
        ├── routes/
        │   └── webhook_routes.py
        │
        └── services/
            └── event_service.py
```

## Implementation Overview

A lightweight payment webhook receiver was developed using FastAPI.

The implementation demonstrates how an application receives and processes payment-related events.

**Endpoint:**

`POST /webhooks/payment`

**Supported events:**

| Event | Purpose |
|---|---|
| payment.success | Processes a successful payment event. |
| payment.failed | Processes a failed payment event. |
| Unknown event | Identifies an unsupported event type. |

**Implementation flow:**

1. The webhook route receives an HTTP POST request.
2. The request payload is extracted as JSON.
3. The event service identifies the event type.
4. The corresponding event-processing logic executes.
5. The application returns an HTTP response.

The implementation uses lightweight event processing without a database, Redis, or Celery.

## Testing

The webhook implementation was tested using Postman.

**Testing covered:**

- Sending a successful payment event.
- Sending a failed payment event.
- Sending an unknown event type.
- Checking the received payload.
- Verifying event-processing output.
- Checking the HTTP response.

**Important testing note:**

Postman was used to simulate a webhook provider by manually sending HTTP POST requests. It did not generate actual payment events.

In a real payment integration, the payment provider automatically sends webhook notifications to the registered endpoint when configured events occur.

## Key Takeaways

- Webhooks provide event-driven communication between applications.
- The provider sends HTTP POST requests when events occur.
- The receiving application processes event payloads through a webhook endpoint.
- Webhooks eliminate the need for continuous polling.
- Signature verification and duplicate-event handling are important concepts in webhook integrations.