#!/usr/bin/python
import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if (level == 'warn'):
                logging.warn( '%s is running.' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@use_logging(level = 'warn')
def foo():
    print('i am foo.')

@use_logging(level = 'error')
def bar():
    print('i am bar.')

foo()
bar()
