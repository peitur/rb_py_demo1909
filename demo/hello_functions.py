#!/usr/bin/env python3

def func1():
    print("[func1] %s" % ( "hello" ) )

def func2( v1 ):
    print("[func2] %s" % ( v1 ) )

def func3( v1, v2 = "default" ):
    print("[func3] %s : %s" % ( v1, v2 ) )

def func4( v1, v2 = "default", **v3 ):
    print("[func4] %s : %s : %s" % ( v1, v2, v3 ) )
    if len( v3 ) > 0:
        print("[func4] v3-length: %d" % ( len( v3 )) )
        for x in v3:
            print( "[func4]\t\t %s : %s" % ( x, v3[x] ) )

def func5( *v1 ):
    for x in v1:
        print("[func5]\t\t %s" % ( x ) )

def func6( v1, *v2, **v3 ):
    print("[func6] v1: %s" % ( v1 ) )
    if len( v2 ) > 0:
        for x in v2:
            print("[func6] v2:\t %s" % ( x ) )

    if len( v3 ) > 0 and is_type( v3, "dict" ):
        for x, y in v3.items():
            print("[func6] v3: \t %s: %s" % ( x, y ) )

def is_type( a, b ):
    if type( a ).__name__ == b:
        return True
    return False

if __name__ == "__main__":

    func1()
    func2( "hello_2_0" )
    func2( v1="hello_2_1" )

    func3( "hello_3_0_0" )
    func3( "Hello_3_0_0", "notdefautl_3_0_1")
    func3( v2="notdefault", v1="hello" )

    func4( "hello_4_0_0", "notdefault_4_0_0", name="test1", type="test", debug=True)
    func4( "hello_4_1_0", "notdefault_4_1_0", debug=True)
    func4( "hello_4_2_0", "notdefault_4_2_0" )


    func5( )
    func5( 101, 102, 103, 104 )
    func5( "aaaa", "bbbb", "cccc" )

    func6( "aaa" )
    func6( "aaa", "zzz", "yyy", "xxx" )
    func6( "aaa",  "zzz", "yyy", "xxx", name="test", type="sample", debug=True )
