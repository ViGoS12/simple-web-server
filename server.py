#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import re

def get(method, url):
    if(method == 'GET'):
        if (url == '/'):
            conn.send(error200.encode())
        elif(url == '/favicon.ico'):            
            conn.send(content.encode())
        elif(url == '/form'):            
            conn.send(form.encode())
        else:
            conn.send(error404.encode())
    elif(method == 'POST'):  
        return 
            

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8080))
serversocket.listen(5)
while True:
    error404 = ("HTTP/1.1 404 Not Found")
    error200 = ("HTTP/1.1 200\nContent-Type: text/html\n\n<h1>Hello World</h1>")
    content = ("HTTP/1.1 200\nContent-Type: image/x-icon\n\n<link rel='icon' type='image/png' href='E:\Site JS\web server\/favicon.ico'>")
    form = ("""HTTP/1.1 200\nContent-Type: text/html\n\n<h1>
        <form action="/form" method='POST'>
            <input type="text" size="40">
            <p><input type="submit"></p>
        </form>
        """)
    conn, addr = serversocket.accept()
    data = conn.makefile()
    print(data)
    print ('Connection:', addr)
    print ('------------------------------')
    print ("Request Data from Browser")
    print ('------------------------------')
    req = data.readline()
    if (req):
        req = re.match(r'(\w+)\s+(.*?)\s+', req)
        method = req[1]
        url = req[2]
        get(method, url)
    conn.close()

            