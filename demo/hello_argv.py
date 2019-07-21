#!/usr/bin/env python3

import getopt
import sys
import os
from pprint import pprint

SUPMODE=("get", "exists", "help")

if __name__ == "__main__":

    ## sys.argv contains all commadn line arguments.
    ## This is a notmal list
    pprint( sys.argv )

    mode = None
    if len( sys.argv ) < 2:
        print("Missing mode")
        print("Supported modes are [%s]"% ( ", ".join( SUPMODE )) )
        sys.exit(1)

    mode = sys.argv[1]

    if mode not in SUPMODE:
        print("Mode '%s' not supported" % ( mode ) )
        print("Supported modes are [%s]"% ( ", ".join( SUPMODE )) )
        sys.exit(2)

    ## If classic commandline arguments are wanted, getopt can parse and suply a classic way of getting the parameters
    try:
        opts, args = getopt.getopt(sys.argv[ 2: ], "hf:o:d", ["help", "output=", "debug", "file=", "url="])
        pprint( opts )
        pprint( args )
    except getopt.GetoptError as err:
        print( err )
        sys.exit(2)

    ## Options default values
    options = dict()
    options["debug"] = False
    options["filename"] = None
    options["output"] = None
    options["url"] = None

    filename_exists = False

    ## Iterate the options lists and values
    for o, a in opts:
        if o in ( "-d", "--debug" ):
            options["debug"] = True

        elif o in ("-o", "--output" ):
            options["output"] = a

        elif o in ("-f", "--file" ):
            options["filename"] = a

        elif o in ( "--url" ):
            options["url"] = a

    if options["filename"]:
        filename_exists = os.path.exists( options["filename"] )

    print("################################################")
    print("Mode : %s" % ( mode ) )
    print("------------------------------------------------")
    pprint( options )
    print("################################################")
