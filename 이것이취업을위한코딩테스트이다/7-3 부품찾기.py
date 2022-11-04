## 방법1 이진 검색로 찾기
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid

        elif target < array[mid]:  ## 중간점보다 크면 앞쪽을 찾아야된다!
            end = mid - 1
        else:
            start = mid + 1
    return None


N=int(sys.stdin.readline())
tool_list=list(map(int,sys.stdin.readline().split(" ")))
M=int(sys.stdin.readline())
check_list=list(map(int,sys.stdin.readline().split(" ")))

tool_list.sort()
print(tool_list)
for c in check_list:
    val=binary_search(tool_list,c,0,N-1)
    if val!=None:
        print("Yes")
    else:
        print("No")

# 방법 2: 계수 정렬로 찾기

# N=int(sys.stdin.readline())
# tool_list=list(map(int,sys.stdin.readline().split(" ")))
# M=int(sys.stdin.readline())
# check_list=list(map(int,sys.stdin.readline().split(" ")))
#
# tool_list.sort()
# print(tool_list)
