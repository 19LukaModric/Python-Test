#!/usr/bin/python
from os.path import abspath
from wsgiref.simple_server import make_server
from paste.deploy import loadapp

if __name__ == '__main__':
    config = 'python_paste.ini'
    appname = 'admin'
    wsgi_app = loadapp('config:%s' % abspath(config), appname)
    server = make_server('20.0.0.11', 8080, wsgi_app)
    server.serve_forever()
