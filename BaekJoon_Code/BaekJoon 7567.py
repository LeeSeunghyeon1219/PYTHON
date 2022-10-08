# 7567변 그릇 문제
import sys
a=sys.stdin.readline().strip()

vv=a[0]
l=10
for v in a[1:]:
    l+=10 if vv!=v else 5
    vv=v
print(l)

