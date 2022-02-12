import sys

N,M=map(int,sys.stdin.readline().split())
x,y,d=list(map(int,sys.stdin.readline().split()))

visited = [[False] * M for _ in range(N)]
visited[x][y]=True
dx=[-1,0,1,0]
dy=[0,1,0,-1]

map=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count=1
turn_time=0
while True:
    ### 왼쪽방향으로 돌기
    d-=1
    if d==-1:
        d=3
    nx=x+dx[d]
    ny=y+dy[d]
    ### 왼쪽방향칸에 가보지도 않았고, 육지인 칸이 존재한다면
    if visited[nx][ny]==False and map[nx][ny]==0:
        x,y=nx,ny
        visited[nx][ny]=True
        count+=1
        turn_time=0
    else:
        turn_time+=1
    ## 네방향으로 모두 갈 수 없다면 뒤로 이동(단,바다이면 안됨)
    if turn_time==4:
        nx = x - dx[d]
        ny = y - dy[d]
        if map[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turn_time=0

print(count)

    ## 만약