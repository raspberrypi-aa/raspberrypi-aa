#!/usr/bin/env python
#
#
#

class Toolbox:
    '''Set of utilities to exercise the power of the Raspberry Pi'''
    
    def get_revision(self):
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                print line
                

