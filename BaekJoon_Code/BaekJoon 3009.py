## BaekJoon 3009 네번째 점

import sys

X_list=[]
Y_list=[]
for _ in range(3):
  X,Y =sys.stdin.readline().split()
  X_list.pop(X_list.index(X))if X in X_list else X_list.append(X)
  Y_list.pop(Y_list.index(Y))if Y in Y_list else Y_list.append(Y)
print(X_list[0],Y_list[0])