import collections


def solution(lottos, win_nums):
    answer = [0,0]

    win_nums_dict = collections.Counter(win_nums)
    lottos_dict = collections.Counter(lottos)

    match_count=0
    for win_num in win_nums_dict.keys():
        if win_num in lottos_dict.keys():
            match_count=match_count+1

    MIN_match = match_count

    MAX_match=match_count+lottos_dict[0]

    match_count_list=[MAX_match,MIN_match]
    for i in range(len(match_count_list)):
        if match_count_list[i]==6:
            answer[i]=1
        elif match_count_list[i]==5:
            answer[i]=2
        elif match_count_list[i]==4:
            answer[i]=3
        elif match_count_list[i]==3:
            answer[i]=4
        elif match_count_list[i]==2:
            answer[i]=5
        else:
            answer[i] = 6


    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]	))


def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]