#!/usr/bin/env python3

if __name__ == "__main__":

    ## empty list of whatever, empty
    str0 = ""
    print( dir( str0 ) )

    print("#################################################")
    print( "[s1] hello %s" % ( "world" ) )
    print( "[s2] hello %30s again" % ( "world" ) )
    print( "[s3] hello %-30s again" % ( "world" ) )
    print( "[s4] hello again for the %d time" % ( 10 ) )
    print( "[s5] hello %(name)s" % {"name":"world" } )
