#!/usr/bin/python3
a = 97
while (a <= 122):
    if (chr(a) == 'e' or chr(a) == 'q'):
        a = a + 1
    else:
        print(chr(a))
        a = a + 1

