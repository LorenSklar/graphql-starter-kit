"""
Main entry point for the unified GraphQL API

This module sets up the GraphQL server using Ariadne and uvicorn.
Serves as the entry point for production deployment on Render.
"""

from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from app.schema import type_defs
from app.resolvers import query, mutation
from app.db import init_database
import os

# Initialize database
init_database()

# Create executable schema
schema = make_executable_schema(type_defs, [query, mutation])

# Create GraphQL app
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    print(f"🚀 Starting Unified GraphQL API on port {port}")
    print(f"📊 GraphQL endpoint: http://localhost:{port}/graphql")
    print(f"🔍 GraphiQL interface: http://localhost:{port}/graphql")
    print(f"✨ Available features: Hello/Ping, Counter, Logs")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    ) 