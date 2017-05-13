#!/usr/bin/env/python
#coding=utf-8
from routes import Mapper
from routes import middleware
import webob.dec
from wsgiref.simple_server import make_server

class controller(object):
    def __init__(self):
        self.i = 1

    def __call__(self):
        print self.i

    def search(self):
        return "do search()"

    def show(self):
        return "do show()"

    def index(self):
        return "do index()"

    def update(self):
        return "do update()"

    def delete(self):
        return "do delete()"

    def create(self):
        return "do create()"

    def create_many(self):
        return "do create_many()"

    def update_many(self):
        return "do update_many()"

    def list_many(self):
        return "do list_many()"

    def delete_many(self):
        return "do delete_many()"

    def preview(self):
        return "do preview()"

class appclass(object):
    def __init__(self):
        a = controller()
        map = Mapper()
        map.resource('message', 'messages', controller=a)
                     #path_prefix='/{projectid}', name_prefix='lala_',
                     #collection={'list_many': 'GET', 'create_many': 'POST'},
                     #member={'update_many': 'POST', 'delete_many': 'POST'},
                     #new={'preview' : 'POST'},
                     #parent_resource=dict(member_name="haha", collection_name="heihei"))
        self.route = middleware.RoutesMiddleware(self.dispatch, map)

    @webob.dec.wsgify
    def __call__(self, req):
        return self.route

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        route = req.environ['routes.route']
        print "route match result is:", match
        if not match:
            return "fake url"
        print "route.name: %s, route.routepath: %s, route.conditions: %s" % (route.name, route.routepath, route.conditions)
        controller = match['controller']
        action = match['action']
        if hasattr(controller, action):
            func = getattr(controller, action)
            ret = func()
            return ret
        else:
            return "has no action:%s" % action

if __name__ == "__main__":
    app = appclass()
    server = make_server('10.0.0.2', 8080, app)
    server.serve_forever()
