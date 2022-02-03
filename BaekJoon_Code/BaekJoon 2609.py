#### 2609 최대공약수와 최소 공배수 - 풀이 1
import sys
a,b=map(int,sys.stdin.readline().split())
result_gcb=1
for i in range(min([a,b]),1,-1):
  if a%i==0 and b%i==0:
    result_gcb=i
    break
print(result_gcb)
print(a*b//result_gcb)