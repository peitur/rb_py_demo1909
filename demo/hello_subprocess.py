#!/usr/bin/env python3

import os, sys, re
import subprocess, shlex

from pprint import pprint

def run( cmd, **opt ):
        result = list()

        if type( cmd ).__name__ == "str":
            cmd = shlex.split( cmd )

        print( "Running: '%s'" % ( " ".join( cmd ) ) )

        prc = subprocess.Popen( cmd, universal_newlines=True, stdout=subprocess.PIPE )
        for line in prc.stdout.readlines():
            result.append( line.lstrip().rstrip() )

        return result


if __name__ == "__main__":
    pprint( run( "ls -al" ) )
