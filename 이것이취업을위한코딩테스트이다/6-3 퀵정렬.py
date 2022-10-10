array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end: # 원소가 1개인 경우 종료
        return
    pivot=start
    left=pivot+1
    right=end
    while left<=right:
        while left<=end and array[left]<=array[pivot]: # pivot 보다 큰 데이터를 찾을 때까지 반복
            left+=1
        while right>start and array[right]>=array[pivot]: # pviot 보다 작은 데이터를 찾을 때까지 반복
            right-=1
        if left>right: # 엇갈렸다면 작은 데이터와 pivot 교체
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
    print(array)

    # 분할이후 각각의 왼쪽 오른쪽 파티션에 대해 정렬 실행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)


