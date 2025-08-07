# Unified GraphQL API

A GraphQL API that combines multiple functionalities:
- **Hello/Ping** - Basic health checks and greetings
- **Counter** - Simple counter with mutations
- **Logs** - Web request log data from SQLite database

## 🚀 Features

- **Unified GraphQL API** with multiple domains
- **Hello/Ping** - Basic queries for testing and health checks
- **Counter** - Stateful counter with increment/set mutations
- **Logs** - Read-only web request logs with filtering and pagination
- **SQLite database** with direct SQL queries (no ORM abstractions)
- **CSV data ingestion** for logs
- **Production-ready** with uvicorn ASGI server

## 📁 Project Structure

```
graphql-starter-kit/
├── app/
│   ├── __init__.py
│   ├── schema.py             # Unified GraphQL schema
│   ├── db.py                 # SQLite database operations
│   └── resolvers.py          # Query and mutation resolvers
├── main.py                   # Entry point (uvicorn)
├── requirements.txt          # Python dependencies
├── rules.md                  # Project rules and requirements
└── README.md
```

## 🛠️ Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python main.py
```

The server starts at: http://localhost:8000/graphql

### 3. Load Sample Data (for logs)

```python
from app.db import load_csv_data
load_csv_data("sample_logs.csv")
```

### 4. Upload Your Own CSV File

To test with your own log data:

1. **Create a CSV file** with the required schema (see CSV Format section below)
2. **Place the file** in your project directory
3. **Load it programmatically**:

```python
from app.db import load_csv_data

# Load your custom CSV file
load_csv_data("your_logs.csv")
```

4. **Or use the utility script**:

```bash
# Edit load_sample_data.py to point to your file
python load_sample_data.py
```

### 📊 Generate Test Data

Need realistic log data for testing? Use the [fake-log-generator](https://github.com/LorenSklar/fake-log-generator) CLI:

```bash
# Clone the fake-log-generator repo (if you haven't already)
git clone https://github.com/LorenSklar/fake-log-generator.git
cd fake-log-generator

# Generate CSV logs with the correct schema for GraphQL API
python generate_logs.py 100 --format csv --output outputs/sample_logs.csv

# Copy the generated file to your GraphQL project
cp outputs/sample_logs.csv ../graphql-starter-kit/

# Return to your GraphQL project
cd ../graphql-starter-kit

# Load the generated data
python load_sample_data.py
```

The fake-log-generator creates realistic synthetic API logs with the exact schema this GraphQL API expects. Perfect for simulating production traffic in development environments.

## 📊 GraphQL Queries & Mutations

### Hello/Ping Queries

```graphql
# Test hello functionality
query testHello {
  hello {
    message
  }
}

# Hello with custom name
query helloWithName {
  hello(name: "Alice") {
    message
  }
}

# Health check ping
query healthCheck {
  ping {
    response
  }
}
```

### Counter Queries & Mutations

```graphql
# Get current counter value
query getCounter {
  counter {
    value
  }
}

# Increment counter by 1
mutation incrementCounter {
  incrementCounter {
    value
  }
}

# Set counter to specific value
mutation setCounter {
  setCounter(value: 100) {
    value
  }
}
```

### Logs Queries

```graphql
# Get logs with pagination and filtering
query getLogs {
  logs(first: 10, offset: 0, log_level: "ERROR", service_name: "user-service") {
    logs {
      id
      TIMESTAMP
      REQUEST_ID
      METHOD
      PATH
      STATUS_CODE
      RESPONSE_TIME_MS
      LOG_LEVEL
      SERVICE_NAME
      ENV
      ERROR_MESSAGE
    }
    total_count
    has_next_page
    has_previous_page
  }
}

# Get single log by ID
query getSingleLog {
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

# Get log statistics and analytics
query getLogStats {
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

## 📝 CSV Format (for logs)

Your CSV file should have these columns:

```csv
TIMESTAMP,REQUEST_ID,METHOD,PATH,QUERY_PARAMETERS,PROTOCOL,SOURCE_IP,USER_AGENT,REFERER,USER_ID,SESSION_ID,REQUEST_HEADERS,REQUEST_BODY,CONTENT_LENGTH,STATUS_CODE,RESPONSE_TIME_MS,RESPONSE_HEADERS,RESPONSE_BODY,LOG_LEVEL,SERVICE_NAME,ENV,ERROR_MESSAGE,STACK_TRACE
2024-01-15T10:30:45.123Z,req_12345,GET,/api/users,{"page":"1","limit":"10"},HTTP/1.1,192.168.1.100,Mozilla/5.0...,https://example.com,user_123,sess_456,{"Accept":"application/json"},,0,200,45,{"Content-Type":"application/json"},{"users":[...]},INFO,user-service,prod,,
```

## 🔮 Future Enhancements

- [ ] REST endpoints for adding single/multiple log entries
- [ ] Authentication and authorization
- [ ] Rate limiting and metering
- [ ] Real-time log streaming
- [ ] Advanced filtering and search
- [ ] Log aggregation and analytics

## 🔐 Authentication & Metering

**When to add authentication:**
- When you have multiple users/tenants
- When log data contains sensitive information
- When you need to track usage per user

**When to add metering:**
- When you want to charge based on usage
- When you need to monitor API usage patterns
- When you want to implement rate limiting

For now, this is a unified API perfect for learning and development.

## 🚀 Deployment

This project is ready for deployment on Render, Railway, or any ASGI-compatible platform.

The `main.py` file serves as the entry point and automatically handles port configuration from environment variables.

## 🛣️ Next Steps

### Immediate (v1.1.0)
- [ ] **Add comprehensive tests** - Unit tests for resolvers, database operations, and API endpoints
- [ ] **Add type hints** - Improve code maintainability and IDE support
- [ ] **Add error handling** - Better error messages and logging
- [ ] **Add code formatting** - Black, flake8, and pre-commit hooks

### Short Term (v1.2.0)
- [ ] **REST endpoints** - Add REST API for log ingestion
- [ ] **Authentication** - JWT-based authentication system
- [ ] **Rate limiting** - API rate limiting and throttling
- [ ] **Database migrations** - Proper migration system for schema changes

### Medium Term (v1.3.0)
- [ ] **Real-time subscriptions** - GraphQL subscriptions for live log streaming
- [ ] **Advanced filtering** - Full-text search and complex query filters
- [ ] **Log aggregation** - Built-in analytics and reporting
- [ ] **Multi-database support** - PostgreSQL, MySQL, and MongoDB options

### Long Term (v2.0.0)
- [ ] **Microservices architecture** - Split into separate services
- [ ] **Kubernetes deployment** - Production-ready containerization
- [ ] **Plugin system** - Extensible architecture for custom log processors
- [ ] **Enterprise features** - Multi-tenancy, SSO, and advanced security

### Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and [CHANGELOG.md](CHANGELOG.md) for version history.

### Documentation
- [API Documentation](docs/API.md) - Detailed GraphQL API reference
- [Examples](examples/) - Ready-to-use GraphQL queries
- [Rules](rules.md) - Project requirements and schema documentation 