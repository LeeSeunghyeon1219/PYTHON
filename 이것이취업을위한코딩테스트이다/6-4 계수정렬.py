array=[1,0,2,3,4,4,8,7,8,6,9]

data=[ 0 for _ in range(max(array)+1)]

for v in array:
    data[v]+=1

print([ i for i in range(len(data)) for _ in range(data[i])])
