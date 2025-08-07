"""
WSGI wrapper for the GraphQL API

This file provides a WSGI-compatible interface for deployments
that require WSGI instead of ASGI.
"""

from asgiref.wsgi import WsgiToAsgi
from main import app

# Convert ASGI app to WSGI
wsgi_app = WsgiToAsgi(app)

# For Gunicorn compatibility
application = wsgi_app 