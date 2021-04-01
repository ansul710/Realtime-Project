import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(2000):
            # self.send(json.dumps({'message': '33'}))
            # self.send(json.dumps({'message': 'HelloWorld22222222'}))
            self.send(json.dumps({'message': randint(1, 1000)}))
            sleep(1)
        self.disconnect(self)


# class WSNewConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#         self.send(json.dumps({'text': 'Connection Successful'}))
#         self.disconnect(self)
