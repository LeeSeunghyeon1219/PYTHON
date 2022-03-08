## 예시3 - 하노이의 탑 재귀함수로 구현하기

def hanoitop(n, start, destination, temp):
    ## 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        print("{0}번 원반을 {1}에서 {2}로 이동".format(n, start, destination))
        return 1
    count = 0
    
    count += hanoitop(n - 1, start, temp, destination) ## 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동
    
    ## 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    print("{0}번 원반을 {1}에서 {2}로 이동".format(n, start, destination))
    count += 1

    count += hanoitop(n - 1, temp, destination, start) # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동

    return count
total_count = hanoitop(3, 1, 3, 2)
print('총 이동 횟수:', total_count)