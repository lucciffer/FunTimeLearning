from __future__ import print_function
msg = input("Enter the message string: ")

ml = len(msg)
for r in range(ml):
    for c in range(r+1):
        print(msg[c],end="")
    print()
