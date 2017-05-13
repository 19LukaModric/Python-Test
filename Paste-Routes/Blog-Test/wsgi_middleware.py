#!/usr/bin/python
from wsgiref.simple_server import make_server
from webob import Request, Response

def display(obj):
    print '-' * 20
    print obj
    print '-' * 20

class SimpleServer(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        res = Response()
        res.status = 200
        res.headerlist = [('Content-type', 'text/plain')]
        res.body = 'Hello World!'
        return res(environ, start_response)

class MiddleWare(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)

server = make_server('10.0.0.2', 8080, MiddleWare(SimpleServer()))
server.serve_forever()
