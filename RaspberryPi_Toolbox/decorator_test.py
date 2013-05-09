#!/usr/bin/env python



def decorator(func):
    def inner_func(func):
        print "Function has been decorated"
        func()
    return inner