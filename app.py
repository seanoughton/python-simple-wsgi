#!/usr/bin/env python3
from wsgiref.simple_server import make_server

def web_app(environment, response):
    status = "200 OK"
    headers =[('Content-type','text/html; charset=utf-8')]
    response(status,headers)
    return [b'<strong>Hello World!!!</strong>']
