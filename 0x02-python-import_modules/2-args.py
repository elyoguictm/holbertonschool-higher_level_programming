#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    if arguments == 1:
        print("{} argument:".format(arguments))
    elif arguments == 0:
        print("{} arguments.".format(arguments))
    else:
        print("{} arguments:".format(arguments))
    for argv in range(arguments):
        print("{}: {}".format(argv + 1, str(sys.argv[argv + 1])))
