#!/usr/bin/env python3

# Json example, parsin.
# ref: https://docs.python.org/3/library/json.html

import sys, os, json, re
from pprint import pprint


def _read_text( filename ):
    result = list()
    try:
        fd = open( filename, "r" )
        for line in fd.readlines():
            result.append( line.lstrip().rstrip() )
        return result
    except Exception as e:
        print("ERROR Reading %s: %s" % ( filename, e ))

    return result

def _read_json( filename ):
    return json.loads( "\n".join( _read_text( filename ) ) )

def load_file( filename ):
    filesplit = re.split( r"\.", filename )
    if filesplit[-1] in ( "json" ):
        return _read_json( filename )
    else:
        return _read_text( filename )



if __name__ == "__main__":

    data = '''
    {
        "name":"test1",
        "type":"sample",
        "debug":"False",
        "tags":[
            "testing",
            "sample",
            "demo"
        ]
    }
    '''

    strct = {"name": "test1",
    "tags": ["testing", "sample", "demo"],
    "type": "sample"}

    print("\n## Json loading, printed as pprint in python format")
    print("\n#--------------------------------------")
    data_py = json.loads( data )
    pprint( data_py )
    print("\n#--------------------------------------")


    print("\n## Structure, printed as json converted from python structure format")
    print("\n#--------------------------------------")
    print( json.dumps( strct ) )
    print("\n#--------------------------------------")
    print( json.dumps( strct, sort_keys=True, indent=4, separators=(',', ': ')))
    print("\n#--------------------------------------")

    if len( sys.argv ) > 1:
        filename = sys.argv[1]
        print("\n## Json taken from file : %s" % (filename) )
        if os.path.exists( filename ):
            pprint( load_file( filename ) )
