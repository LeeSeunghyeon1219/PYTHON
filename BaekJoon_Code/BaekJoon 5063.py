import sys

i=int(sys.stdin.readline())

for _ in range(i):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('advertise')