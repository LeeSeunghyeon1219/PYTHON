import sys

i=int(sys.stdin.readline())

Q1,Q2,Q3,Q4,axis=0,0,0,0,0
for _ in range(i):
    x,y=map(int,sys.stdin.readline().split())

    if x==0 or y==0:
        axis+=1
    elif x>0 and y>0:
        Q1+=1
    elif x<0 and y>0:
        Q2+=1
    elif x<0 and y<0:
        Q3+=1
    elif x>0 and y<0:
        Q4+=1

print("Q1: {0}".format(Q1))
print("Q2: {0}".format(Q2))
print("Q3: {0}".format(Q3))
print("Q4: {0}".format(Q4))
print("AXIS: {0}".format(axis))