import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class CommentConsumer(WebsocketConsumer):
    def connect(self):

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            "all", self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        pass

    def comment(self, event):
        self.send(json.dumps(
            {
                'type': 'comment',
                'content': event['content']
            })
        )



