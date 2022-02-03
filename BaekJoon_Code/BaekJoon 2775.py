## 2775 부녀회장이 될테야
T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    if n==1:
        print("1")
        continue
    room_people=[val for val in range(1,n+1)]
    for kk in range(k):
        for nn in range(1,n):
            room_people[nn]+=room_people[nn-1]
    print(room_people[n-1])