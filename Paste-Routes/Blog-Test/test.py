#!/usr/bin/env/python
from webob import Request, Response
import webob.exc
import webob.dec

from routes import Mapper
from routes import middleware

from wsgiref.simple_server import make_server

class Controller(object):
    @webob.dec.wsgify
    def __call__(self, req):
        res = Response()
        res.status = 200
        res.body = 'Hello World!'
        return res

class MyApp(object):
    def __init__(self):
        super(MyApp, self).__init__()
        self.map = Mapper()
        self.map.connect('/luka', controller = Controller(), action = 'show')
        self.router = middleware.RoutesMiddleware(self.dispatch, self.map)

    @webob.dec.wsgify
    def __call__(self, req):
        print '---------before match:'
        urll = ['%s : %s' % (k,v) for k,v in sorted(req.environ.items())]
        print '\n'.join(urll)
        return self.router

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        print '---------after match:'
        urll = ['%s : %s' % (k,v) for k,v in sorted(req.environ.items())]
        print '\n'.join(urll)
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()

        app = match['controller']
        return app

app = MyApp()
print app
print 'Listen port on 8000'
server = make_server('20.0.0.51', 8888, app)
server.serve_forever()
