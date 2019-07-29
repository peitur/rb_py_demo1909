#!/usr/bin/env python3

import sys,re,os,re, datetime
import urllib.request
import json

from pprint import pprint

def get_pypi_url( module = "" ):
    return "https://pypi.python.org/pypi/%s/json" % ( module )

def get_request( url , **opt ):
    x_size = 0
    l_size = 0
    r_size = 0
    bsize=1024
    overwrite = False
    timeout = 10

    if 'bsize' in opt: bsize = opt['bsize']
    if 'timeout' in opt: timeout = opt['timeout']

    req = urllib.request.Request( url = url )
    data = None
    with urllib.request.urlopen(req) as f:
        if f.status != 200:
            raise RuntimeError("Could not load url : %s, got %s" % ( modurl, f.status ))
        data = f.read().decode('utf-8')
        return json.loads( data )

    return None

if __name__ == "__main__":
    modurl = get_pypi_url( "ipaddress" )
    json_data = get_request( modurl )

    pprint( json_data.keys() )
    pprint( sorted( json_data['releases'] ) )
    pprint( json_data["releases"]["1.0.22"] )
