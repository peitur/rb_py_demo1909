#!/usr/bin/env python3

import os, sys
import random
import string

from pprint import pprint

SPECIAL="!#%=.,-_"

def random_string( length ):
    return ''.join(random.SystemRandom().choice( SPECIAL + string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range( length ))

def has_lowercase( block ):
    pass

def has_uppercase( block ):
    pass

def has_number( block ):
    pass

def has_special( block ):
    pass

if __name__ == "__main__":
    opt = dict()

    if len( sys.argv ) < 3:
        print("%s <blocks> <block-len>" %( sys.argv[0] ))
        sys.exit(1)

    nblocks = int( sys.argv[1] )
    blength = int( sys.argv[2] )
