#!/usr/bin/env python3

if __name__ == "__main__":

    ## empty list of whatever, empty
    list0 = list()
    list1 = []

    list3 = ["a", "b", "c","d" ]


    print("############# LIST ##############")
    print("Sample [%s]: %s" % ( len(list3), list3 ) )

    print("## Print list as is:")
    for x in list3:
        print(x)

    print("## Sorted list:")
    for x in sorted( list3 ):
        print(x)

    print("## Print list enumerated:")
    for a, b  in enumerate( list3 ):
        print( "%s => %s" % (a, b) )

    print("############# DICTS ##############")
    ## empty dictionary, empty
    dict0 = dict()
    dict1 = {}
