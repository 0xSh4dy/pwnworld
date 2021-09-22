### About the chat application
We will not store any message in the database. We'll use Django channels to create an efficient chat application

#### ASGI: 
ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications. WSGI applications are a single, synchronous callable that takes a request and returns a response; this doesn’t allow for long-lived connections, like you get with long-poll HTTP or WebSocket connections. That's why ASGI is used.

#### Channels:
Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.

#### Consumers:
Consumers are to channels as views are to Django



