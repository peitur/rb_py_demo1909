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
        sys.exit(1)

    mode = sys.argv[1]

    if mode not in SUPMODE:
        print("Mode '%s' not supported" % ( mode ) )

    ## If classic commandline arguments are wanted, getopt can parse and suply a classic way of getting the parameters
    try:
        opts, args = getopt.getopt(sys.argv[ 2: ], "hf:o:d", ["help", "output=", "debug", "file="])
        pprint( opts )
        pprint( args )
    except getopt.GetoptError as err:
        print( err )
        sys.exit(2)

    ## Options default values
    debug = False
    filename = None
    filename_exists = False
    output = None

    ## Iterate the options lists and values
    for o, a in opts:
        if o in ( "-d", "--debug" ):
            verbose = True

        elif o in ("-o", "--output"):
            output = a

        elif o in ("-f", "--file"):
            filename = a


    if filename:
        filename_exists = os.path.exists( filename )

    print("################################################")
    print("Mode : %s" % ( mode ) )
    print("Debug : %s" % ( debug ) )
    print("Output : %s" % ( output ) )
    print("File : %s [%s]" % ( filename, filename_exists ) )
