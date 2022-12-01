#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if argv == 0:
        print("0 argument")
    elif argv == 1:
        print("1 argument")
    else:
        print("{} arguments:".format(n))

        for i in rang(n):
            print("{}: {}".format(i + 1, argv[i + 1]))
