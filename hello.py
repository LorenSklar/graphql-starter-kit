"""
Hello and Ping GraphQL API

This module provides basic GraphQL queries for:
- hello(name: String): Returns a personalized greeting
- ping: Health check endpoint that returns "pong"

Usage:
    python hello.py
    
The server will start on http://localhost:5050/graphql
You can test queries in GraphiQL or any GraphQL client.

Example queries:
    query { hello(name: "Alice") }
    query { ping }
"""

from ariadne import QueryType, gql, make_executable_schema
from ariadne.wsgi import GraphQL

type_defs = gql("""
    type Query {
        hello(name: String): String!
        ping: String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info, name=None):
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"

@query.field("ping")
def resolve_ping(*_):
    return "pong"

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Port 5050 used to avoid conflicts with other dev servers
    server = make_server("0.0.0.0", 5050, app)
    print("🚀 Serving on http://localhost:5050/graphql")
    server.serve_forever()
