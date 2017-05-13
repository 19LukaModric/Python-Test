#!/usr/bin/python
from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import *
from webob.exc import *

class MyRequest(Request):
    @property
    def is_host(self):
        return self.remote_addr == '10.0.0.1'

@wsgify(RequestClass = MyRequest)
def TestDec(req):
    if req.is_host:
        res = Response()
        res.status = 200
        res.headerlist = [('Content-type', 'text/plain')]
        res.body = 'Hello World!'
        return res
    else:
        raise HTTPForbidden

class SimpleApp(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        req = Request(environ)
        return TestDec(environ, start_response)

server = make_server('10.0.0.2', 8080, SimpleApp())
server.serve_forever()
