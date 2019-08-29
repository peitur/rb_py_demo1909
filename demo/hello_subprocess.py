#!/usr/bin/env python3

import os, sys, re
import subprocess, shlex

from pprint import pprint

def run( cmd, **opt ):
        result = list()
        debug = False
        if 'debug' in opt and opt['debug'] in (True, False):
            debug = opt['debug']

        if type( cmd ).__name__ == "str":
            cmd = shlex.split( cmd )

        if debug: print( "Running: '%s'" % ( " ".join( cmd ) ) )

        prc = subprocess.Popen( cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines=True )
        for line in prc.stdout.readlines():
            result.append( line.lstrip().rstrip() )

        return result


if __name__ == "__main__":

    cmds = ["ls -al","ls -al wekf", "dmesg"]
    for cmd in cmds:
        print("%s\n> Running command: '%s' <\n%s" % ( "\n%s" % ( "-"*40 ), cmd, "-"*40 ))
        pprint( run( cmd ) )
        print("%s%s" % (">"*20, "<"*20) )
