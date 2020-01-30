import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTING_MODULE", "delivery.settings")
channel_layer = get_channel_layer()