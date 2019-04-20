#!/usr/bin/env python3
from wsgiref.simple_server import make_server

def web_app(environment, response):
    status = "200 OK"
    headers =[('Content-type','text/html; charset=utf-8')]
    response(status,headers)
    return [b'<strong>Hello World!!!</strong>']

# with server argumenst(host(defaults to localhost, port, function to run))
with make_server('localhost',3000,web_app) as server:
    print('Serving on port 3000 ...\n visit http://127.0.0.1:3000/\n to kill the server Ctrl+C')
    server.serve_forever()
# environment - CGI styles variable
# response - status, headers,
# status variable must be 4 characters long
# headers - a list with tuples
