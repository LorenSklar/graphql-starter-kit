"""
Counter GraphQL API

This module provides a simple counter with GraphQL queries and mutations:
- counter: Returns the current counter value
- incrementCounter: Increments counter by 1
- setCounter(value: Int!): Sets counter to a specified value

Usage:
    python counter.py
    
The server will start on http://localhost:5050/graphql
You can test queries and mutations in GraphiQL or any GraphQL client.

Example queries:
    query { counter }
    
Example mutations:
    mutation { incrementCounter }
    mutation { setCounter(value: 100) }

Note: Counter state is global and not thread-safe. For production, consider using a database or Redis.
"""

from ariadne import gql, QueryType, MutationType, make_executable_schema
from ariadne.wsgi import GraphQL

# === SCHEMA DEFINITION ===
type_defs = gql("""
    type Query {
        counter: Int!
    }

    type Mutation {
        incrementCounter: Int!
        setCounter(value: Int!): Int!
    }
""")

# === QUERY RESOLVERS ===
# Counter query with initial value set to 0
counter_query = QueryType()

state = {"count": 0}

@counter_query.field("counter")
def resolve_counter(*_):
    return state["count"]

# === MUTATION RESOLVERS ===
# Counter mutation to increment or set the counter value
counter_mutation = MutationType()

@counter_mutation.field("incrementCounter")
def resolve_increment(*_):
    state["count"] += 1
    return state["count"]

@counter_mutation.field("setCounter")
def resolve_set_counter(_, info, value):
    state["count"] = value
    return state["count"]

# === SCHEMA SETUP ===
schema = make_executable_schema(type_defs, [counter_query, counter_mutation])

# === APP SETUP ===
app = GraphQL(schema, debug=True)

# === SERVER SETUP ===
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Port 5050 used to avoid conflicts with other dev servers
    server = make_server("0.0.0.0", 5050, app)
    print("🚀 Serving on http://localhost:5050/graphql")

    server.serve_forever()
