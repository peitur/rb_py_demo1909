#!/usr/bin/env python3

import os, sys, re
import subprocess, shlex

from pprint import pprint

ALLOWED_COMMANDS=["shasum", "sha1sum","sha256sum", "sha512sum", "md5sum", "cat", "grep"]
NOT_ALLOWED_CHAR=["|", ">", "<", ";"]


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
            result.append( line )
            if prc.poll():
                break

        return (prc.returncode, result)



def run_yield( cmd, **opt ):
        debug = False
        if 'debug' in opt and opt['debug'] in (True, False):
            debug = opt['debug']

        if type( cmd ).__name__ == "str":
            cmd = shlex.split( cmd )

        if debug: print( "Running: '%s'" % ( " ".join( cmd ) ) )

        prc = subprocess.Popen( cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines=True )
        for line in prc.stdout.readlines():
            yield line.rstrip()

            if prc.poll():
                break



if __name__ == "__main__":
    pass
