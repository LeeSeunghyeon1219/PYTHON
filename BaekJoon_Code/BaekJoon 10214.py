import sys
T=int(sys.stdin.readline())
for _ in range(T):
    Y,K=0,0
    for i in range(9):
        y,k=map(int,sys.stdin.readline().split())
        Y+=y
        K+=k
    if Y>K:
        print("Yonsei")
    elif Y<K:
        print("Korea")
    else:
        print("Draw")
