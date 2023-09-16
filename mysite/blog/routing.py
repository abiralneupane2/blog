from django.urls import re_path

from blog import consumers

websocket_urlpatterns = [
    re_path(r"ws/", consumers.CommentConsumer.as_asgi()),
]