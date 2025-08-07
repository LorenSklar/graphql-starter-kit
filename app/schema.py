"""
GraphQL schema definition for the unified API

This module defines the GraphQL types and queries for:
- Hello/Ping functionality
- Counter with mutations
- Logs with filtering and pagination
"""

from ariadne import gql

# GraphQL schema definition
type_defs = gql("""
    # Hello/Ping types
    type HelloResponse {
        message: String!
    }

    type PingResponse {
        response: String!
    }

    # Counter types
    type Counter {
        value: Int!
    }

    # Log types
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

    type LogsConnection {
        logs: [Log!]!
        total_count: Int!
        has_next_page: Boolean!
        has_previous_page: Boolean!
    }

    type LogStats {
        total_logs: Int!
        logs_by_level: [LevelCount!]!
        logs_by_service: [ServiceCount!]!
        logs_by_status: [StatusCount!]!
        logs_by_env: [EnvCount!]!
    }

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

    # Root Query type
    type Query {
        # Hello/Ping queries
        hello(name: String): HelloResponse!
        ping: PingResponse!
        
        # Counter queries
        counter: Counter!
        
        # Logs queries
        logs(
            first: Int = 100
            offset: Int = 0
            log_level: String
            service_name: String
            status_code: Int
            env: String
        ): LogsConnection!
        
        log(id: ID!): Log
        logStats: LogStats!
    }

    # Root Mutation type
    type Mutation {
        # Counter mutations
        incrementCounter: Counter!
        setCounter(value: Int!): Counter!
    }
""") 