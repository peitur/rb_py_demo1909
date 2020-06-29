#!/bin/bash

import string

if __name__ == "__main__":

    for x in range(33, 127):
        print( "%s > %s" % ( x, chr(x) ) )

    for x in string.digits+string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase:
        z = ord('0')
        y = ord(x) ^ z
        print("%s > %s xor %s => %s" % ( x, ord(x), bin(z), y ) )
