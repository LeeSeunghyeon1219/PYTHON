## BaekJoon 1181 단어정렬
import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
    ##### input이 입력이 느려서  이거 쓰면 속도 빨라짐!
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)