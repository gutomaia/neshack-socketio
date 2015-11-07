import redis
from json import loads
from json import dumps

from socketio.namespace import BaseNamespace
from socketio import socketio_manage
import socket


def index(request):
    """ Base view to load our template """
    return {}


class GameNamespace(BaseNamespace):

    def listener(self):
        r = redis.StrictRedis()
        r = r.pubsub()
        r.subscribe('game')

        for m in r.listen():
            if m['type'] == 'message':
                data = loads(m['data'])
                self.emit('game', data)

    def on_subscribe(self, *args, **kwargs):
        self.spawn(self.listener)

    def on_game(self, msg):
        pass

    def on_hack(self, msg):
        UDP_IP = '127.0.0.1'
        UDP_PORT = 53474

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(dumps(msg)), (UDP_IP, UDP_PORT))


def socketio_service(request):
    retval = socketio_manage(request.environ,
        {
            '': GameNamespace,
        }, request=request
    )

    return retval
