import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from uvicorn_pr.consumer import 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uvicorn_pr.settings')
router = URLRouter(
    [
        path('ws/echo', EchoWebsocketConsumer.as_asgi())
    ]
)
django_app = get_asgi_application()
application = ProtocolTypeRouter(
    {
        'http': django_app,
        'websocket': ...
    }
)