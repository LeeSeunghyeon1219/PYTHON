## 큰수의 법칙
## 다양한 수로 배열이 있을 때, 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
## 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없음
N,M,K=map(int,input().split())
num_list=list(map(int,input().split()))
num_list.sort()
max_val=num_list[-1]
max_val2=num_list[-2]

### 방법1 반복문 사용하기
result=0
for i in range(1,M+1):
    result+=max_val2 if i%K==0 else max_val
print(result)

### 방법2 수식 만들기
count=(M//(K+1))*K+M%(K+1)
result= count*max_val+(M-count)*max_val2

print(result)


