#!/usr/bin/env python3

from pprint import pprint
if __name__ == "__main__":

    ## empty list of whatever, empty
    list0 = list()

    print("\n# Supported object fuctions and functionality")
    pprint( dir( list0 ) )

    ## creting a simple list of numbers
    list1 = [ 103, 101, 108, 114, 105 ]

    ## reference copy of list1
    list2 = list1

    ## copying the list into a new list (copy, not reference)
    list3 = list1.copy()

    print("\n# start list")
    pprint( list1 )

    list1.append( 201 )
    list1.append( 202 )
    list2.reverse()

    print("\n# original list, appendded 2 elements and reversed")
    pprint( list1 )

    ## list comprehension,
    print("\n# list comprehension")
    pprint( [ x + x for x in list1 ] )

    ## map funciton, takes a transform (map) function and a list (or iterable) object
    print("\n# map funciton result")
    pprint( list( map( lambda x: x + x, list1 ) ) )

    ## Since we copied list1 to list2, it's not just a reference.
    print( "\n# list2, created as reference")
    pprint( list2 )

    print("\n# list3, copy of list1")
    pprint( list3 )
