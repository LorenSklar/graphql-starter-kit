from ariadne import QueryType, gql, make_executable_schema
from ariadne.wsgi import GraphQL

type_defs = gql("""
    type Query {
        hello(name: String): String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info, name=None):
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Port 5050 used to avoid conflicts with other dev servers
    server = make_server("0.0.0.0", 5050, app)
    print("🚀 Serving on http://localhost:5050/graphql")
    server.serve_forever()
