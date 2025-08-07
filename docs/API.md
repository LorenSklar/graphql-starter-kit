# GraphQL API Documentation

This document provides detailed information about the GraphQL API endpoints, types, and usage examples.

## Overview

The GraphQL API provides three main functional areas:
- **Hello/Ping**: Basic health checks and greetings
- **Counter**: Stateful counter with mutations
- **Logs**: Web request log data with filtering and pagination

## Base URL

```
http://localhost:8000/graphql
```

## Schema

### Hello/Ping Types

#### HelloResponse
```graphql
type HelloResponse {
  message: String!
}
```

#### PingResponse
```graphql
type PingResponse {
  response: String!
}
```

### Counter Types

#### Counter
```graphql
type Counter {
  value: Int!
}
```

### Log Types

#### Log
```graphql
type Log {
  id: ID!
  TIMESTAMP: String!
  REQUEST_ID: String
  METHOD: String
  PATH: String
  QUERY_PARAMETERS: String
  PROTOCOL: String
  SOURCE_IP: String
  USER_AGENT: String
  REFERER: String
  USER_ID: String
  SESSION_ID: String
  REQUEST_HEADERS: String
  REQUEST_BODY: String
  CONTENT_LENGTH: Int
  STATUS_CODE: Int
  RESPONSE_TIME_MS: Int
  RESPONSE_HEADERS: String
  RESPONSE_BODY: String
  LOG_LEVEL: String
  SERVICE_NAME: String
  ENV: String
  ERROR_MESSAGE: String
  STACK_TRACE: String
  created_at: String!
}
```

#### LogsConnection
```graphql
type LogsConnection {
  logs: [Log!]!
  total_count: Int!
  has_next_page: Boolean!
  has_previous_page: Boolean!
}
```

#### LogStats
```graphql
type LogStats {
  total_logs: Int!
  logs_by_level: [LevelCount!]!
  logs_by_service: [ServiceCount!]!
  logs_by_status: [StatusCount!]!
  logs_by_env: [EnvCount!]!
}
```

#### Statistics Types
```graphql
type LevelCount {
  level: String!
  count: Int!
}

type ServiceCount {
  service: String!
  count: Int!
}

type StatusCount {
  status_code: Int!
  count: Int!
}

type EnvCount {
  env: String!
  count: Int!
}
```

## Queries

### Hello/Ping Queries

#### hello
Returns a greeting message.

**Arguments:**
- `name: String` (optional) - Name to include in the greeting

**Returns:** `HelloResponse`

**Example:**
```graphql
query {
  hello(name: "Alice") {
    message
  }
}
```

**Response:**
```json
{
  "data": {
    "hello": {
      "message": "Hello, Alice!"
    }
  }
}
```

#### ping
Health check endpoint.

**Arguments:** None

**Returns:** `PingResponse`

**Example:**
```graphql
query {
  ping {
    response
  }
}
```

**Response:**
```json
{
  "data": {
    "ping": {
      "response": "pong"
    }
  }
}
```

### Counter Queries

#### counter
Returns the current counter value.

**Arguments:** None

**Returns:** `Counter`

**Example:**
```graphql
query {
  counter {
    value
  }
}
```

**Response:**
```json
{
  "data": {
    "counter": {
      "value": 42
    }
  }
}
```

### Logs Queries

#### logs
Retrieves logs with pagination and filtering.

**Arguments:**
- `first: Int` (optional, default: 100) - Number of records to return
- `offset: Int` (optional, default: 0) - Number of records to skip
- `log_level: String` (optional) - Filter by log level
- `service_name: String` (optional) - Filter by service name
- `status_code: Int` (optional) - Filter by status code
- `env: String` (optional) - Filter by environment

**Returns:** `LogsConnection`

**Example:**
```graphql
query {
  logs(first: 10, offset: 0, log_level: "ERROR") {
    logs {
      id
      TIMESTAMP
      METHOD
      PATH
      STATUS_CODE
      LOG_LEVEL
      SERVICE_NAME
    }
    total_count
    has_next_page
    has_previous_page
  }
}
```

#### log
Retrieves a single log by ID.

**Arguments:**
- `id: ID!` - Log ID

**Returns:** `Log`

**Example:**
```graphql
query {
  log(id: "1") {
    id
    TIMESTAMP
    REQUEST_ID
    METHOD
    PATH
    SOURCE_IP
    USER_AGENT
    STATUS_CODE
    RESPONSE_TIME_MS
    LOG_LEVEL
    SERVICE_NAME
    ENV
  }
}
```

#### logStats
Returns log statistics and analytics.

**Arguments:** None

**Returns:** `LogStats`

**Example:**
```graphql
query {
  logStats {
    total_logs
    logs_by_level {
      level
      count
    }
    logs_by_service {
      service
      count
    }
    logs_by_status {
      status_code
      count
    }
    logs_by_env {
      env
      count
    }
  }
}
```

## Mutations

### Counter Mutations

#### incrementCounter
Increments the counter by 1.

**Arguments:** None

**Returns:** `Counter`

**Example:**
```graphql
mutation {
  incrementCounter {
    value
  }
}
```

**Response:**
```json
{
  "data": {
    "incrementCounter": {
      "value": 43
    }
  }
}
```

#### setCounter
Sets the counter to a specific value.

**Arguments:**
- `value: Int!` - New counter value

**Returns:** `Counter`

**Example:**
```graphql
mutation {
  setCounter(value: 100) {
    value
  }
}
```

**Response:**
```json
{
  "data": {
    "setCounter": {
      "value": 100
    }
  }
}
```

## Error Handling

The API returns GraphQL errors in the standard format:

```json
{
  "errors": [
    {
      "message": "Error description",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": ["queryName"]
    }
  ],
  "data": null
}
```

### Common Error Codes

- **400**: Bad Request - Invalid query syntax
- **404**: Not Found - Log ID not found
- **500**: Internal Server Error - Database or server error

## Rate Limiting

Currently, no rate limiting is implemented. This may be added in future versions.

## Authentication

Currently, no authentication is required. This may be added in future versions.

## Pagination

Log queries support cursor-based pagination using `first` and `offset` parameters:

- `first`: Number of records to return (max 1000)
- `offset`: Number of records to skip
- `has_next_page`: Boolean indicating if more records are available
- `has_previous_page`: Boolean indicating if previous records are available

## Filtering

Log queries support filtering by:

- **log_level**: INFO, DEBUG, WARN, ERROR
- **service_name**: Name of the service
- **status_code**: HTTP status code
- **env**: Environment (prod, dev, staging, etc.)

Multiple filters can be combined.

## Examples

See the `examples/` directory for complete query examples that can be copied and pasted into GraphiQL.

## Testing

Use GraphiQL (available at http://localhost:8000/graphql) to test queries interactively.

## Versioning

This API follows semantic versioning. Breaking changes will be documented in the CHANGELOG.md file. 