#!/usr/bin/env python3

##########################################################
## Part 1, simpole loops
##########################################################
def loop_part1():
    pass

##########################################################
## Part 2, looping structures
##########################################################
def loop_part2():
    ## empty list of whatever, empty
    list0 = list()
    list1 = []

    list3 = ["a", "b", "c","d" ]


    print("############# LIST ##############")
    print("Sample [%s]: %s" % ( len(list3), list3 ) )

    print("\n## Print list as is:")
    for x in list3:
        print(x)

    print("\n## Sorted list:")
    for x in sorted( list3 ):
        print(x)

    print("\n## Print list enumerated:")
    for a, b  in enumerate( list3 ):
        print( "%s => %s" % (a, b) )

    print("############# DICTS ##############")
    ## empty dictionary, empty
    dict0 = dict()
    dict1 = {}




if __name__ == "__main__":

    ##########################################################
    ## Part 1, simpole loops
    ##########################################################



    ##########################################################
    ## Part 2, looping structures
    ##########################################################
    loop_part2()

    ##########################################################
    ## Part 3, iterators
    ##########################################################
