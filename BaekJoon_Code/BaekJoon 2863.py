## BaekJoon 2863 - 5와 6의 차이
import sys
A,B=sys.stdin.readline().split()
print(int(A.replace("6","5"))+int(B.replace("6","5")), end=" ")
print(int(A.replace("5","6"))+int(B.replace("5","6")))



