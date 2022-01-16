####################################################
def solution(participant, completion):
    answer = ''

    dic = {}
    for member in participant:
        dic[member]=0
    for member in participant:
        dic[member] = dic[member]+1

    for member in completion:
        dic[member] = dic[member] - 1

    for member in list(dic.keys()):
        if dic[member] > 0:
            return member

print(solution(['leo','kiki','eden'],['eden','kiki']))

#################################################### 다른사람 코드 예시

import collections


def solution(participant, completion):
    ###  collections.counter 함수: 리스트 내용을 key로 하여 갯수를 센다.
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
print(solution(['leo','kiki','eden'],['eden','kiki']))
