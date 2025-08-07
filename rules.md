# Project Rules & Requirements

## API Structure
The project provides a unified GraphQL API with three main domains:

1. **Hello/Ping** - Basic health checks and greetings
2. **Counter** - Stateful counter with mutations
3. **Logs** - Web request log data from SQLite

## Schema Structure (for logs)
The CSV file contains web request logs with the following columns:

```csv
TIMESTAMP,REQUEST_ID,METHOD,PATH,QUERY_PARAMETERS,PROTOCOL,SOURCE_IP,USER_AGENT,REFERER,USER_ID,SESSION_ID,REQUEST_HEADERS,REQUEST_BODY,CONTENT_LENGTH,STATUS_CODE,RESPONSE_TIME_MS,RESPONSE_HEADERS,RESPONSE_BODY,LOG_LEVEL,SERVICE_NAME,ENV,ERROR_MESSAGE,STACK_TRACE
```

## Database Schema
- Use SQLite with direct SQL queries (no SQLAlchemy)
- Table name: `logs`
- All fields should match the CSV structure exactly

## GraphQL API
- **Hello/Ping**: Read-only queries for testing
- **Counter**: Read queries + mutations (increment, set)
- **Logs**: Read-only with filtering by LOG_LEVEL, SERVICE_NAME, STATUS_CODE, ENV
- Support pagination for logs
- Include statistics queries for logs

## File Structure
```
graphql-starter-kit/
├── app/
│   ├── __init__.py
│   ├── schema.py             # Unified GraphQL schema
│   ├── db.py                 # SQLite database operations
│   └── resolvers.py          # Query and mutation resolvers
├── main.py                   # Entry point (uvicorn)
├── requirements.txt          # Python deps
├── rules.md                  # This file
└── README.md
```

## Future Enhancements
- REST endpoints for adding single/multiple log entries
- Authentication and authorization
- Rate limiting and metering
- Separate microservices if needed 