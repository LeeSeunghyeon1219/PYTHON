## BaekJoon 2839 설탕배달
import sys

num = int(sys.stdin.readline())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break
    num -= 3
    count += 1
else:
    print(-1)