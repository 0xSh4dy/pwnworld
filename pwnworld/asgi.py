import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import tools.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pwnworld.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            tools.routing.websocket_urlpatterns
        )
    ),
})