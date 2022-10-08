import sys

i=int(sys.stdin.readline())
a=sys.stdin.readline().strip()

A=a.count("A")
B=a.count("B")

if A>B:
    print("A")
elif A<B:
    print("B")
else:
    print("Tie")