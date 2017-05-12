#!/usr/bin/python

class ShowVersion(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        print 'app:ShowVersion is called.'
        start_response("200 OK",[("Content-type", "text/plain")])
        return ['Version = 1.0.0',]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print 'in ShowVersion.factory', global_conf, kwargs
        return ShowVersion()

class LogFilter(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print 'filter:LogFilter is called.'
        return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in LogFilter.factory", global_conf, kwargs
        return LogFilter
