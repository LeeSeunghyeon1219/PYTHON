### BaekJoon 4673 셀프 넘버
num_list=set(range(1,10001))
remove_list=set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    remove_list.add(i)
num_list=num_list-remove_list
for k in sorted(num_list):
    print(k)
