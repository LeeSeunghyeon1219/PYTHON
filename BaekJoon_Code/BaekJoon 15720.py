## BaekJoon 15720 - 카우버거
import sys

B,C,D=map(int,sys.stdin.readline().split())
burger_list=sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
side_list=sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
drink_list=sorted(list(map(int,sys.stdin.readline().split())),reverse=True)


print(sum(burger_list)+sum(side_list)+sum(drink_list))
idx=min(B,C,D)
print(int(sum(burger_list[:idx]+side_list[:idx] +drink_list[:idx])*0.9)+sum(burger_list[idx:]+side_list[idx:]+drink_list[idx:]))