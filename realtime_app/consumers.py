import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(10, -1, -1):
            self.send(json.dumps({'message': i}))
            sleep(1)
        self.close()


# class WSNewConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#         self.send(json.dumps({'text': 'Connection Successful'}))
#         self.disconnect(self)
