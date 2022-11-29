#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print("{}".format(a))
    else:
        print(f"{a:0>2}", end=", ")
