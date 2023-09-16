import json

from channels.generic.websocket import WebsocketConsumer


class CommentConsumer(WebsocketConsumer):
    def connect(self):

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            "all", self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        pass



