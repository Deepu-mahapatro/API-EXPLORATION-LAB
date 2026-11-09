# OData API (Open Data Protocol)

## 1. Overview

OData (Open Data Protocol) is an open protocol that allows applications to create, access, and manipulate data through standardized REST-based APIs.

It is built on web technologies such as HTTP and commonly uses JSON for data representation.

OData provides a standardized way to interact with data sources without requiring clients to understand their internal database structures.

It defines conventions for querying, filtering, sorting, creating, updating, and deleting data.

**Why was OData introduced?**

Different applications often expose data using different API structures and query formats.

OData was introduced to standardize how clients access and manipulate data through web APIs.

It allows clients to interact with different data sources using a consistent set of rules and query options.

## 2. Purpose

OData is designed to simplify and standardize data access through REST-based communication.

Its main purposes are:

- Provide standardized data access through HTTP.
- Allow clients to filter and sort data.
- Support querying and retrieving specific data.
- Enable CRUD operations on resources.
- Reduce the need for custom query endpoints.
- Provide a common interface for accessing different data sources.

**Example:**

Consider an e-commerce application containing thousands of products.

A client may need only products belonging to a particular category, sorted by price.

OData allows the client to specify these requirements through standardized query options rather than requiring a separate API endpoint for every query.

## 3. Core Components

OData contains several important components.

### 3.1 Entity Data Model (EDM)

EDM defines the logical structure of the data exposed by an OData service.

It describes entities, properties, relationships, and other data types.

**Purpose:**
- Defines the data model.
- Describes entity structures.
- Defines relationships between entities.
- Provides a standardized representation of service data.

### 3.2 Entity

An Entity represents an individual data object in an OData service.

It generally contains properties that describe the object.

**Example:**

A Product entity may contain:

- Product ID
- Product Name
- Price
- Category

### 3.3 Entity Set

An Entity Set represents a collection of entities of the same type.

**Example:**

A Products entity set contains multiple Product entities.

### 3.4 Properties

Properties represent individual attributes of an entity.

They define the data stored within an entity.

**Example:**

A Product entity may contain:

- `ProductID`
- `ProductName`
- `Price`

### 3.5 Relationships

Relationships define how different entity types are connected.

Common relationship types include:

- One-to-One
- One-to-Many
- Many-to-Many

**Example:**

One customer can have multiple orders.

### 3.6 Navigation Properties

Navigation Properties allow clients to move between related entities.

**Example:**

A client can navigate from a Customer entity to its related Orders.

### 3.7 Service Document

The Service Document provides information about the available entity sets exposed by an OData service.

It helps clients discover the resources they can access.

### 3.8 Metadata Document

The Metadata Document describes the structure of an OData service.

It provides information about:

- Entity types.
- Properties.
- Relationships.
- Entity sets.
- Data types.
- Service operations.

OData commonly exposes metadata through the `$metadata` endpoint.

### 3.9 Query Options

Query Options allow clients to control how data is retrieved and processed.

They support filtering, sorting, selecting fields, and other query operations.

### 3.10 OData Service

An OData Service exposes data through standardized HTTP endpoints.

It processes client requests and returns data according to the OData conventions.

## 4. Architecture

OData follows a client-server architecture based on REST principles.

### OData Architecture Diagram

```text id="odataflow1"
          Client Application
                 |
                 |
          HTTP Request
                 |
                 v
           OData Service
                 |
                 v
          Request Processing
                 |
                 v
          OData Query Parser
                 |
                 v
           Entity Data Model
                 |
                 v
             Data Source
                 |
                 v
          Response Generation
                 |
                 v
          JSON / XML Response
                 |
                 v
          Client Application
```

### Architecture Components

**1. Client Application**

The application that requests data from an OData service.

It can retrieve, filter, sort, create, update, or delete resources.

**2. OData Service**

Receives HTTP requests and processes them according to OData standards.

**3. Query Parser**

Interprets OData query options and determines how the requested data should be retrieved.

**4. Entity Data Model**

Defines the structure and relationships of the exposed data.

**5. Data Source**

Contains the actual application data, such as database records.

**6. Response Generator**

Formats the processed result into an appropriate response representation, commonly JSON.

## 5. Internal Working

OData communication works through the following steps.

### Step 1: Service Discovery

The client accesses the OData Service Document to identify the available resources.

### Step 2: Metadata Discovery

The client retrieves the metadata document to understand the data model.

It identifies available entities, properties, relationships, and data types.

### Step 3: Request Creation

The client prepares an HTTP request for the required resource.

It can include OData query options to control the returned data.

### Step 4: Request Transmission

The client sends the HTTP request to the OData service.

### Step 5: Request Processing

The OData service identifies the requested resource and interprets the query options.

### Step 6: Data Retrieval

The service accesses the corresponding data source and retrieves the requested information.

### Step 7: Query Processing

The service applies operations such as filtering, sorting, selecting properties, or pagination.

### Step 8: Response Generation

The service formats the result, commonly as JSON, and generates an HTTP response.

### Step 9: Client Reception

The client receives and processes the response.

**Complete communication flow:**

```text id="odataflow2"
Client
  |
  | 1. Discover Service
  |
  | 2. Read Metadata
  |
  | 3. Send HTTP Request
  |
  v
OData Service
  |
  | 4. Parse Query Options
  |
  | 5. Access Data Source
  |
  | 6. Process Requested Data
  |
  | 7. Generate Response
  |
  v
Client
  |
  | 8. Process JSON Response
  |
  v
Requested Data
```

## 6. Functions and Features

OData provides standardized operations and query capabilities.

### 6.1 CRUD Operations

OData supports the common data manipulation operations.

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Creates a new resource. |
| Read | GET | Retrieves a resource. |
| Update | PUT / PATCH | Replaces or modifies a resource. |
| Delete | DELETE | Removes a resource. |

### 6.2 Filtering ($filter)

The `$filter` query option retrieves only records that satisfy a specified condition.

**Example concept:**

Retrieve products whose price is greater than 500.

### 6.3 Selecting Properties ($select)

The `$select` option retrieves only the requested properties of an entity.

**Example concept:**

Retrieve only product names and prices instead of all product details.

### 6.4 Sorting ($orderby)

The `$orderby` option sorts the returned records based on a specified property.

It supports ascending and descending order.

### 6.5 Pagination ($top and $skip)

These options control how many records are returned and which records are skipped.

- `$top` specifies the maximum number of records to return.
- `$skip` specifies the number of records to skip.

They help retrieve large datasets in smaller portions.

### 6.6 Counting ($count)

The `$count` option allows clients to retrieve the number of matching records.

This is useful when applications need to display total record counts.

### 6.7 Expanding Related Data ($expand)

The `$expand` option retrieves related entities along with the requested entity.

**Example concept:**

Retrieve a customer together with the customer's orders.

### 6.8 Search ($search)

The `$search` option allows clients to search for resources based on supported search expressions.

Its exact behavior depends on the OData version and service implementation.

### 6.9 Metadata Discovery

OData provides metadata describing the service's available entities, properties, relationships, and operations.

This helps clients understand the API without relying entirely on separate documentation.

### 6.10 Batch Requests

OData supports batch requests that allow multiple operations to be grouped into a single HTTP request.

This can reduce the number of network round trips required by clients.

## 7. Communication Mechanism

OData uses HTTP-based REST communication to exchange data between clients and services.

### 7.1 HTTP Methods

OData uses standard HTTP methods for resource operations.

- GET – Retrieve resources.
- POST – Create resources.
- PUT – Replace resources.
- PATCH – Partially update resources.
- DELETE – Remove resources.

### 7.2 Data Formats

OData supports standardized data representations.

**JSON:**

- Commonly used for data exchange.
- Lightweight and easy to process.
- Widely supported by modern applications.

**XML:**

- Used in OData metadata documents.
- Represents structured service definitions.
- Also supported for data representations in applicable OData versions and formats.

### 7.3 Endpoint Structure

An OData service commonly exposes:

| Endpoint | Purpose |
|---|---|
| Service Root | Entry point of the OData service. |
| Service Document | Lists available entity sets. |
| `$metadata` | Describes the service data model. |
| Entity Set | Provides access to a collection of entities. |
| Entity Resource | Provides access to an individual entity. |

### 7.4 Standard Query Options

| Query Option | Purpose |
|---|---|
| `$filter` | Filters records. |
| `$select` | Selects specific properties. |
| `$orderby` | Sorts records. |
| `$top` | Limits the number of records. |
| `$skip` | Skips records. |
| `$count` | Returns a record count. |
| `$expand` | Includes related entities. |
| `$search` | Searches resources. |

These options allow clients to express data requirements through standardized URL query parameters.

## 8. Advantages

1. **Standardized Data Access:** Provides common conventions for retrieving and manipulating data across different services.

2. **Flexible Querying:** Supports filtering, sorting, pagination, and selecting specific properties without requiring separate custom endpoints.

3. **Metadata Discovery:** Allows clients to understand available data structures and relationships through standardized metadata.

## 9. Disadvantages

1. **Query Complexity:** Advanced query options and relationships can make requests difficult to understand and manage.

2. **Performance Considerations:** Complex filtering, expansion, and large queries can increase server and database workload.

3. **Implementation Complexity:** Supporting OData standards and query capabilities requires additional service-side configuration and validation.

## 10. Use Cases

OData is suitable for applications that need standardized access to structured business data.

### 10.1 Enterprise Applications

Used to expose business data from enterprise systems through standardized APIs.

### 10.2 Business Intelligence

Allows reporting applications to retrieve filtered and selected business information.

### 10.3 ERP Systems

Used to expose information related to products, inventory, orders, and business operations.

### 10.4 CRM Systems

Supports access to customer details, contacts, activities, and sales information.

### 10.5 Data Integration

Allows different applications to access and exchange structured information through a common interface.

### 10.6 Microsoft Ecosystem

OData is used in several Microsoft technologies and services, including Microsoft Dataverse and related enterprise data integrations.

### 10.7 Analytical Applications

Useful for applications that need to retrieve selected records and related information from large datasets.

---

## Key Takeaways

- OData is a standardized protocol for accessing and manipulating data through REST-based APIs.
- It uses HTTP for communication and commonly uses JSON for data exchange.
- Entity Data Model defines the structure and relationships of service data.
- Metadata helps clients discover available entities, properties, and relationships.
- Query options such as `$filter`, `$select`, `$orderby`, and `$expand` provide flexible data retrieval.
- OData supports CRUD operations through standard HTTP methods.
- It is commonly used in enterprise applications, ERP systems, CRM systems, and data integration.