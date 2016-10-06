
class GreenError (Exception):
    pass

class BlueError (Exception):
    pass

class RedError (Exception):
    pass

class ErrorThrower (object):
    
    def __init__(self,error_lst):
        self.pos = -1
        self.error_lst  = error_lst

    def throw(self):
        self.pos += 1
        raise self.error_lst[self.pos]


def foo(thrower):
    print("starting foo")
    try:
        bar(thrower)
    except BlueError:
        print("foo caught a BlueError")
    bar(thrower)
    print("returning from foo")

def bar(thrower):
    print("starting bar")
    try:
        fraz(thrower)
    except GreenError:
        print("bar caught a GreenError")
    print("returning from bar")

def fraz(thrower):
    print("starting fraz")
    try:
        # Team Leader says what EXCEPTION to raise here
        raise thrower.throw()     
        print("after the exception in fraz")
    except RedError:
        print("fraz caught a RedError")
    print("returning from fraz")

def main():
    thrower = ErrorThrower([BlueError(), RedError(), GreenError(), IndexError()])
    try:
        foo(thrower)
        bar(thrower)
        fraz(thrower)
    except BlueError:
        print("main caught a BlueError")
    except RedError:
        print("main caught a RedError")
    print("returning from main")
    
main()
