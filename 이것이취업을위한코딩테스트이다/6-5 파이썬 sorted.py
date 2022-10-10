array=[5,7,9,0,3,1,6,2,4,8]

array=sorted(array)
print(array)

array=[[2,0],[0,2],[0,1],[1,0]]
array=sorted(array,key=lambda x: (x[0],x[1]))
print(array)