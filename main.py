from ariadne import gql, QueryType, MutationType, make_executable_schema
from ariadne.wsgi import GraphQL

# === SCHEMA DEFINITION ===
type_defs = gql("""
    type Query {
        ping: String!
        hello(name: String): String!
        counter: Int!
    }

    type Mutation {
    incrementCounter: Int!
    setCounter(value: Int!): Int!
    }

    """)

# === QUERY RESOLVERS ===
# Ping query to check if the server is running
ping_query = QueryType()
@ping_query.field("ping")
def resolve_ping(*_):
    return "pong"

# Hello query that takes an optional name argument
hello_query = QueryType()

@hello_query.field("hello")
def resolve_hello(_, info, name=None):
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"

# Counter query with initial value set to 0
counter_query = QueryType()

state = {"count": 0}

@counter_query.field("counter")
def resolve_counter(*_):
    return state["count"]

# Merge query resolvers into a single QueryType
query = [ping_query, hello_query, counter_query]

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

# Merge mutation resolvers into a single MutationType
mutation = [counter_mutation]

# === SCHEMA SETUP ===
schema = make_executable_schema(type_defs, [*query, *mutation])

# === APP SETUP ===
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Port 5050 used to avoid conflicts with other dev servers
    server = make_server("0.0.0.0", 5050, app)
    print("🚀 Serving on http://localhost:5050/graphql")

    server.serve_forever()
