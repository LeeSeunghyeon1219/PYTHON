## BaekJoon 18228 - 팽귄추락대책위원회
import sys
N=int(sys.stdin.readline())
ice_list=list(map(int,sys.stdin.readline().split()))

panguin_idx=ice_list.index(-1)
print(min(ice_list[0:panguin_idx])+min(ice_list[panguin_idx+1:]))

