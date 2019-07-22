#!/usr/bin/env python3

import sys
from pprint import pprint

if __name__ == "__main__":

    print("your message")
    print("your message", file=sys.stdout )
    print("your message", file=sys.stderr)
    print("your message", end="" )
