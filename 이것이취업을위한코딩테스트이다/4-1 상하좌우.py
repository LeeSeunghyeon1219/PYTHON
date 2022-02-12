### 상하좌우
## 여행가 A는 N × N 크기의 정사각형 공간 위에 서 있다.
## 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상(1, 1)이다.
## 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다
## 계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다
## L: 왼쪽으로 한 칸 이동 R: 오른쪽으로 한 칸 이동 U: 위로 한 칸 이동 D: 아래로 한 칸 이동
## 이때 여행가 A가 N × N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다
import sys

N=int(sys.stdin.readline())
move_list=list(sys.stdin.readline().strip().split())
move_dict={"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}
x,y=1,1
for move in move_list:
    nx=x+move_dict[move][0]
    ny=y+move_dict[move][1]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x,y=nx,ny
print(x,y)

##### 답안 예시
n=int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny >n:
        continue
    x,y = nx,ny
print(x,y)