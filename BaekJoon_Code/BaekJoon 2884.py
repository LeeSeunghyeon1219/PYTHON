# BaekJoon 2884 알람시계 45분 일찍 맞추기

H,M=map(int, input().split())

if M>=45 and M<=59:
    print(H, M-45)
else:
    if H==0:
        print(23,M+60-45)
    else:
        print(H-1,M+60-45)