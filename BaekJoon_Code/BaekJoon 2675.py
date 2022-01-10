# BaekJoon 2675
T=int(input())
data= [list(input().split()) for _ in range(T)]

for i in range(T):
    P=""
    R,S=data[i]
    for s in S:
        P=P+s*int(R)
    print(P)