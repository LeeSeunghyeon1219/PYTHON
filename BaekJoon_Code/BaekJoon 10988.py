import sys

val=sys.stdin.readline().strip()
print(1 if val==val[::-1] else 0)