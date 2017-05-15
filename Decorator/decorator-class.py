#!/usr/bin/python
import logging

class use_logging(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        logging.warn('%s is running.' % self._func.__name__)
        self._func()

@use_logging
def bar():
    print('i am bar.')

bar()
