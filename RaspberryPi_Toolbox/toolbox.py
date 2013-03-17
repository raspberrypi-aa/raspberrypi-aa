#!/usr/bin/env python
#
#
#

class UnknownRevision(Exception):
    pass

class Toolbox:
    '''Set of utilities to exercise the power of the Raspberry Pi'''
    def __init__(self):
        pass
    
    def get_revision(self):
        'Return Model and Revision of the current board'
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if 'Revision' in line:
                    rev = line.split(':')[1].strip()
                    #print rev
                    if rev == '0002':
                        return 'Model B'
                    elif rev == '0003':
                        return 'Model B'
                    elif rev == '0004':
                        pass
                    elif rev == '0005':
                    elif rev == '0006':
                    elif rev == '0007':
                    elif rev == '0008':
                    elif rev == '0009':
                    elif rev == '000d':
                    elif rev == '000e':
                    elif rev == '000f':
                    else:
                        raise UnknownRevision('Revision is: ' + rev)
                


if __name__ == '__main__':
    t = Toolbox()
    t.get_revision()