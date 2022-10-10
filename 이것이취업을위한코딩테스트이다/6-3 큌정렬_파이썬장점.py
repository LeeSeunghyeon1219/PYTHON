array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort(left_side) +[pivot]+quick_sort(right_side)
print(quick_sort(array))