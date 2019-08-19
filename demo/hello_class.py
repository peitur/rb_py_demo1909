#!/usr/bin/env python3

from pprint import pprint

class Test1( object ):

    def __init__( self, param ):
        self._param = param
        self._type = type( param ).__name__

    def getType( self ):
        return self._type

    def getParam( self ):
        return self._param

    def __str__( self ):
        return "%s:%s" % ( self._param.__str__(), self._type.__str__() )

    def create( param ):
        return Test1( param )


if __name__ == "__main__":

    print( Test1( "test" ) )

    print( Test1.create( "hello" ) )
