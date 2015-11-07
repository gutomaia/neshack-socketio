#!/usr/bin/env python
from pyramid.config import Configurator
from neshack_socketio.views import socketio_service
from neshack_socketio.views import index

def simple_route(config, name, url, fn):
    config.add_route(name, url)
    config.add_view(
        fn, route_name=name,
        renderer="neshack_socketio:templates/%s.mako" % name)


def main(global_config, **settings):
    config = Configurator()
    config.include('pyramid_mako')

    config.add_static_view(name='static/js', path='neshack_spa:static')
    config.add_static_view(name='static/css', path='neshack_spa:static')


    simple_route(config, 'index', '/', index)
    simple_route(config, 'socket_io', 'socket.io/*remaining', socketio_service)

    config.add_static_view('static/old', 'static', cache_max_age=3600)

    app = config.make_wsgi_app()

    return app
