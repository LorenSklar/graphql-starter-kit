# Hello Ariadne - My First GraphQL API

A simple GraphQL API using **Ariadne** that supports a ping health check, a hello world query, and a global counter with mutation support.

## 🚀 Features

* `hello(name: String)`: Returns a greeting.
* `ping`: Health check that returns `"pong"`.
* `counter`: Returns the current counter value.
* `incrementCounter`: Increments counter by 1.
* `setCounter(value: Int!)`: Sets counter to a specified value.

---

## 🛠️ Getting Started

### 1. Clone and Install

```bash
git clone <your-repo-url>
cd ariadne-counter
pip install ariadne
```

### 2. Run the Server

```bash
python app.py
```

This starts a GraphQL server at:
[http://localhost:5050/graphql](http://localhost:5050/graphql)

---

## 🧪 Using GraphiQL

The server automatically loads **GraphiQL**, a web-based IDE for GraphQL.

### First Query

In GraphiQL, paste and run:

```graphql
query {
  hello(name: "Alice")
}
```

Expected response:

```json
{
  "data": {
    "hello": "Hello, Alice!"
  }
}
```

### First Mutation

Set the counter to a specific value:

```graphql
mutation {
  setCounter(value: 100)
}
```

Expected response:

```json
{
  "data": {
    "setCounter": 100
  }
}
```

Then query the counter value:

```graphql
query {
  counter
}
```

Response:

```json
{
  "data": {
    "counter": 100
  }
}
```

---

## 📄 File Overview

| File           | Purpose                                   |
| -------------- | ----------------------------------------- |
| `app.py`       | Main entrypoint, runs WSGI server         |
| `schema.gql`   | (Optional) Move type\_defs here if needed |
| `queries.py`   | (Optional) Modular query resolvers        |
| `mutations.py` | (Optional) Modular mutation resolvers     |

---

## 🔧 Notes

* Counter state is global and not thread-safe. For production, consider using a database or Redis.
* Uses WSGI for simplicity. Switch to `ariadne.asgi.GraphQL` for async or production.


