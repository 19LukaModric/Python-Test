#!/usr/bin/python
#coding:utf-8
import eventlet

def handle(fd):
    print "client connected"
    while True:   #典型的读取文件的操作
        # pass through every non-eof line
        x = fd.readline()
        if not x: break
        fd.write(x)
        fd.flush()         #将文件内容刷新到硬盘中
        print "echoed", x,
    print "client disconnected"


print "server socket listening on port 8000"   #服务器监听程序，响应客户端的请求
server = eventlet.listen(('127.0.0.1', 8000))  # (IP地址， 端口) 元祖的形式表示
pool = eventlet.GreenPool(200)    #绿色线程池，允许并行访问

while True:
        new_sock, address = server.accept() #阻塞，等待客户端连接，返回socket对象和客户端的IP地址和端口号
        print "accepted", address
        pool.spawn_n(handle, new_sock.makefile('rw'))  #创建新的绿色线程然后去执行
        print 'pool.running:', pool.running()
        print 'pool.free', pool.free()
