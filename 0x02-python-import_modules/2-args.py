#!/usr/bin/python3
# prints the number of and the list of its arguments
if _name_ == "_main_":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
                print("{}: {}".format(i, arg[i]))

            elseif size == 0:
                        print("{} arguments:".format(size))
                    else:                       
                        print("{} arguments:".format(size))
                        print("{}: {}".format(i, arg[1]))
