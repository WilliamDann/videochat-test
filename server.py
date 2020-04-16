import websockets
import asyncio
import time
import sys
import json

# Take in a video stream
class StreamServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.users = set

        # the current frame to show
        self.frame = None

        self.viewSocket   = websockets.serve(self.run, host, port)
        self.streamSocket = websockets.serve(self.streamer, host, port+1)

    # start the server
    def start(self):
        asyncio.get_event_loop().run_until_complete(self.viewSocket)
        asyncio.get_event_loop().run_until_complete(self.streamSocket)

        asyncio.get_event_loop().run_forever()

    # handle stream
    async def streamer(self, websocket, path):
        while True:
            try:
                self.frame = websocket.recv()

                await asyncio.sleep(0.01)
            except websockets.ConnectionClosed as e:
                break
            
    # handle stream data
    async def run(self, websocket, path):
        # Register.
        self.users.add(websocket)
        try:
            while True:
                await websocket.send(str(json.dumps(self.users)))
                await asyncio.sleep(0.01)
        finally:
            # Unregister.
            self.users[websocket] = None

server = StreamServer('localhost', 8080)
server.start()