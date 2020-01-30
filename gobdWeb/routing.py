from channels.routing import route
from main.consumers import ws_connect, ws_receive

ASGI_APPLICATION = "gobdWeb.asgi.application"

channel_routing = [
    # websocket channels to store consumers
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),
]
