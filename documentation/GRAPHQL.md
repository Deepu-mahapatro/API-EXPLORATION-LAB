# GraphQL API

## 1. Overview

GraphQL is a query language and runtime for APIs developed by Facebook.

It allows clients to request exactly the data they need from a server through a single endpoint.

Unlike traditional REST APIs, GraphQL allows clients to retrieve multiple related resources in a single request.

## 2. Purpose

GraphQL is designed to solve common API data-fetching problems.

Its main purposes are:

- Allow clients to request specific data.
- Reduce unnecessary data transfer.
- Retrieve related resources through a single request.
- Provide a flexible API structure.
- Simplify data fetching for frontend applications.

## 3. Core Components

| Component | Description |
|---|---|
| Schema | Defines the structure and capabilities of the API. |
| Type | Defines the structure of available data. |
| Query | Retrieves data from the server. |
| Mutation | Creates, updates, or deletes data. |
| Resolver | Contains the logic for retrieving or modifying data. |
| Arguments | Pass additional information to queries and mutations. |

## 4. Architecture

GraphQL follows a client-server architecture.

```text
       Client Application
              |
              | GraphQL Request
              v
       GraphQL Endpoint
              |
              v
         GraphQL Schema
              |
              v
           Resolver
              |
              v
        Data Source
              |
              v
        Response to Client
```

**Main flow:**

1. Client sends a GraphQL request.
2. GraphQL validates the request against the schema.
3. The appropriate resolver executes.
4. Resolver retrieves or modifies the data.
5. GraphQL returns the requested response.

## 5. Internal Working

GraphQL processes requests through the following steps:

1. **Request:** The client sends a query or mutation to the GraphQL endpoint.
2. **Parsing:** GraphQL parses the incoming request.
3. **Validation:** The request is checked against the schema.
4. **Execution:** GraphQL executes the corresponding resolver functions.
5. **Data Retrieval:** Resolvers interact with the data source.
6. **Response:** The server returns the requested data in JSON format.

## 6. Functions and Features

**Important GraphQL operations and features:**

- **Query:** Retrieves data.
- **Mutation:** Creates, updates, and deletes data.
- **Resolver:** Handles the execution logic for fields.
- **Arguments:** Pass parameters to queries and mutations.
- **Schema:** Defines available operations and data structures.
- **Input Types:** Define structured input data for mutations.
- **Fragments:** Reuse common fields across queries.
- **Aliases:** Request the same field multiple times with different names.
- **Introspection:** Allows clients to explore the API schema.

## 7. Communication Mechanism

GraphQL commonly communicates over HTTP.

- Uses a single endpoint, usually `/graphql`.
- Supports HTTP POST for queries and mutations.
- Uses JSON for request and response data.
- The client specifies which fields it needs.
- The server returns the requested fields.

**Example endpoint:**

`http://127.0.0.1:8000/graphql`

## 8. Advantages

1. **Flexible Data Fetching:** Clients request only the required fields.
2. **Single Endpoint:** Multiple operations can be handled through one endpoint.
3. **Reduced Network Requests:** Related data can be retrieved in a single request.

## 9. Disadvantages

1. **Complexity:** Schema and resolver management require additional understanding.
2. **Query Performance:** Complex or deeply nested queries can increase server workload.
3. **Caching Challenges:** Traditional HTTP caching can be more difficult because many operations use one endpoint.

## 10. Use Cases

GraphQL is suitable for:

- Applications requiring flexible data fetching.
- Social media platforms.
- E-commerce applications.
- Mobile applications with limited network bandwidth.
- Dashboards requiring data from multiple resources.
- Applications with frequently changing frontend data requirements.

---

# Practical Implementation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend framework |
| Strawberry GraphQL | GraphQL implementation for Python |
| Uvicorn | ASGI server |
| Postman | API testing |

## Project Structure

```text
API-EXPLORATION-LAB/
│
└── apps/
    └── graphql_api/
        └── main.py
```

## Implementation Overview

The GraphQL API was implemented using FastAPI and Strawberry.

A simple **User Management System** was selected to understand GraphQL operations.

The implementation includes:

| Operation | Purpose |
|---|---|
| users | Retrieve all users |
| user(id) | Retrieve a specific user |
| createUser | Create a new user |
| updateUser | Update an existing user |
| deleteUser | Delete a user |
| hello | Test the GraphQL endpoint |

The implementation uses in-memory storage. Data is not permanently stored in a database.

## Testing

The API was tested using Postman.

**Testing covered:**

- Retrieving all users.
- Retrieving a user by ID.
- Creating a user.
- Updating user details.
- Deleting a user.
- Testing the basic hello query.

**GraphQL endpoint:**

`http://127.0.0.1:8000/graphql`

**Swagger documentation:**

`http://127.0.0.1:8000/docs`

## Key Takeaways

- GraphQL allows clients to request specific data.
- Queries retrieve data, while mutations modify data.
- Resolvers execute the business logic behind GraphQL operations.
- Schema defines the structure and capabilities of a GraphQL API.
- Strawberry integrates GraphQL with Python and FastAPI.