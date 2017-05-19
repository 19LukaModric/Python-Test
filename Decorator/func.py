import foo
def wrapper():
    filename = 'func.py'
    def show_filename():
        return 'filename:%s' % filename

    print show_filename.__globals__
    print foo.call_func(show_filename)

wrapper()
