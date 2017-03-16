#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name == '' or name == None:
        name = 'World'
    result = ''.join(['Hello, ', name, '!'])
    return result

print(hello())