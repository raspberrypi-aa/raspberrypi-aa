#!/usr/bin/env python
#
#
#

class Toolbox:
    '''Set of utilities to exercise the power of the Raspberry Pi'''
    def __init__(self):
        pass
    
    def get_revision(self):
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if 'Revision' in line:
                    rev = line.split(':')
                    print rev[1].strip()
                


if __name__ == '__main__':
    t = Toolbox()
    t.get_revision()