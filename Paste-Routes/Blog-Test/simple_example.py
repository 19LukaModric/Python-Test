#!/usr/bin/python

from wsgiref.simple_server import make_server

def application(environ, start_response):

    response_body = ['Hello World!']

    content_length = 0
    for s in response_body:
        content_length += len(s)

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(content_length))]
    start_response(status, response_headers)

    return response_body

httpd = make_server('20.0.0.11', 8080, application)
httpd.serve_forever()
