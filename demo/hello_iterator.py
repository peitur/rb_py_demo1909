#!/usr/bin/env python3

import random

from pprint import pprint

def rand_int( n, max=100 ):
    for i in range( n ):
        yield random.randint(1, max )


class RandomInteger( object ):
    def __init__( self, n, max ):
        self._num = n
        self._maxval = max

    def __iter__( self ):
        for i in range( self._num ):
            yield random.randint(1, self._maxval )



if __name__ == "__main__":

    for i in rand_int( 10, 69 ):
        print( i )

    print( "# ---------------------------------- ")
    for x in RandomInteger( 10, 99 ):
        print( x )
