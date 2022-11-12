
d=[0]*100

def pibo(x):

    d[0]=0
    d[1]=1
    for i in range(2,x+1):
        d[i]=d[i-1]+d[i-2]
    return d[x]

print(pibo(6))