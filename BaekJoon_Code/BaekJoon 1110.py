## BaekJoon 1110 더하기 사이클
import sys

N=int(sys.stdin.readline())
val=N
cnt=0
while True:
  if cnt!=0 and val==N: break
  val=(val%10*10)+(((val//10)+(val%10))%10)
  cnt+=1
print(cnt)