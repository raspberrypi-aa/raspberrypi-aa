#!/usr/bin/env python

import time

debounce_time = .2        # 200 ms
button_last_action = 0

def do_something():
    pass

if (time.time() - button_last_action > debounce_time):
    button_last_action = time.time()
    do_something()




### Class format

class Button:
    def __init__(self, debounce_time, action):
        self.debounce_time_sec = debounce_time
        self.button_last_action = 0
        self.callback = action

    def button_pressed():
        now = time.time()
        if (now - self.button_last_action > self.debounce_time_sec):
            self.button_last_action = now
            return self.callback()



#
# Usage
# 
x = Button(.2, do_something)
x.button_pressed()




