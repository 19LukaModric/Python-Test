#!/usr/bin/env/python
import eventlet
from eventlet.green import urllib2

def sum(num1, num2):
    return num1 + num2

num = [(1, 2), (2, 4)]
pool = eventlet.GreenPool(200)
result = pool.starmap(sum, num)

print '-' * 20
print result
print '-' * 20

for body in result:
    print body

print pool.running()
print pool.free()
