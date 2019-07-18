#!/usr/bin/env python3

def func1():
    print("[func1] %s" % ( "hello" ) )

def func2( v1 ):
    print("[func2] %s" % ( v1 ) )

def func3( v1, v2 = "default" ):
    print("[func3] %s : %s" % ( v1, v2 ) )

def func4( v1, v2 = "default", **v3 ):
    print("[func3] %s : %s : %s" % ( v1, v2, v3 ) )


if __name__ == "__main__":
    func1()
    func2( "hello" )
    func3( "hello" )
    func3( "Hello", "notdefautl")
