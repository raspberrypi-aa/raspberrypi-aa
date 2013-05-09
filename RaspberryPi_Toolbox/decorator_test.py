#!/usr/bin/env python



def decorator(func):
    def inner_func(func):
        print "Function has been decorated"
        func()
    return inner_func(func)
    
@decorator
def test_func(a):
    print "Value is", str(a)
    
    
test_func(10)