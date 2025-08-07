"""
GraphQL resolvers for the unified API

This module contains the resolver functions that handle GraphQL queries
and mutations for hello/ping, counter, and logs functionality.
"""

from ariadne import QueryType, MutationType
from .db import get_logs, get_log_count, get_db_connection

# Create QueryType and MutationType for resolvers
query = QueryType()
mutation = MutationType()

# Global counter state
counter_state = {"value": 0}

# Hello/Ping resolvers
@query.field("hello")
def resolve_hello(_, info, name=None):
    """
    Resolve hello query
    """
    if name:
        return {"message": f"Hello, {name}!"}
    return {"message": "Hello, World!"}

@query.field("ping")
def resolve_ping(_, info):
    """
    Resolve ping query
    """
    return {"response": "pong"}

# Counter resolvers
@query.field("counter")
def resolve_counter(_, info):
    """
    Resolve counter query
    """
    return {"value": counter_state["value"]}

@mutation.field("incrementCounter")
def resolve_increment_counter(_, info):
    """
    Resolve increment counter mutation
    """
    counter_state["value"] += 1
    return {"value": counter_state["value"]}

@mutation.field("setCounter")
def resolve_set_counter(_, info, value):
    """
    Resolve set counter mutation
    """
    counter_state["value"] = value
    return {"value": counter_state["value"]}

# Logs resolvers
@query.field("logs")
def resolve_logs(_, info, first=100, offset=0, log_level=None, service_name=None, status_code=None, env=None):
    """
    Resolve logs query with pagination and filtering
    """
    # Get logs from database
    logs = get_logs(limit=first, offset=offset, log_level=log_level, service_name=service_name, status_code=status_code, env=env)
    
    # Get total count for pagination info
    total_count = get_log_count(log_level=log_level, service_name=service_name, status_code=status_code, env=env)
    
    # Calculate pagination info
    has_next_page = (offset + first) < total_count
    has_previous_page = offset > 0
    
    return {
        "logs": logs,
        "total_count": total_count,
        "has_next_page": has_next_page,
        "has_previous_page": has_previous_page
    }

@query.field("log")
def resolve_log(_, info, id):
    """
    Resolve single log query by ID
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM logs WHERE id = ?", (id,))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return dict(row)
    return None

@query.field("logStats")
def resolve_log_stats(_, info):
    """
    Resolve log statistics query
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get total count
    cursor.execute("SELECT COUNT(*) FROM logs")
    total_logs = cursor.fetchone()[0]
    
    # Get counts by log level
    cursor.execute("""
        SELECT LOG_LEVEL, COUNT(*) as count 
        FROM logs 
        WHERE LOG_LEVEL IS NOT NULL 
        GROUP BY LOG_LEVEL 
        ORDER BY count DESC
    """)
    logs_by_level = [
        {"level": row[0], "count": row[1]} 
        for row in cursor.fetchall()
    ]
    
    # Get counts by service name
    cursor.execute("""
        SELECT SERVICE_NAME, COUNT(*) as count 
        FROM logs 
        WHERE SERVICE_NAME IS NOT NULL 
        GROUP BY SERVICE_NAME 
        ORDER BY count DESC
    """)
    logs_by_service = [
        {"service": row[0], "count": row[1]} 
        for row in cursor.fetchall()
    ]
    
    # Get counts by status code
    cursor.execute("""
        SELECT STATUS_CODE, COUNT(*) as count 
        FROM logs 
        WHERE STATUS_CODE IS NOT NULL 
        GROUP BY STATUS_CODE 
        ORDER BY count DESC
    """)
    logs_by_status = [
        {"status_code": row[0], "count": row[1]} 
        for row in cursor.fetchall()
    ]
    
    # Get counts by environment
    cursor.execute("""
        SELECT ENV, COUNT(*) as count 
        FROM logs 
        WHERE ENV IS NOT NULL 
        GROUP BY ENV 
        ORDER BY count DESC
    """)
    logs_by_env = [
        {"env": row[0], "count": row[1]} 
        for row in cursor.fetchall()
    ]
    
    conn.close()
    
    return {
        "total_logs": total_logs,
        "logs_by_level": logs_by_level,
        "logs_by_service": logs_by_service,
        "logs_by_status": logs_by_status,
        "logs_by_env": logs_by_env
    } 