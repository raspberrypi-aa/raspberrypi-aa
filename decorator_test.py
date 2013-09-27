#!/usr/bin/env python


def decorator(func):
    def inner_func(x):
        print "Function has been decorated"
        func(x)
    return inner_func
    
@decorator
def test_func(a):
    print "Value is", str(a)
    
    
test_func(10)