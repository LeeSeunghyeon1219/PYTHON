## BaekJoon 1018 체스판

import sys
N, M = map(int, sys.stdin.readline().split())
chess= [sys.stdin.readline().strip() for _ in range(N)]
result_val=N*M
for i in range(N-7):
    for j in range(M-7):
        black=0
        white=0
        for ii in range(i,i+8):
            for jj in range(j,j+8):
                if (ii + jj) % 2 == 0:
                    if chess[ii][jj] != 'W': black += 1
                    if chess[ii][jj] != 'B': white += 1
                else:
                    if chess[ii][jj] != 'B': black += 1
                    if chess[ii][jj] != 'W': white += 1
        result_val = min(black,white) if min(black,white)<result_val else result_val
print(result_val)