# 2022 KAKAO BLIND RECRUITMENT 신고결과받기

import collections

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report = list(set(report))
    report.sort()

    report_count_list = []
    for report_val in report:
        report_count_list.append(report_val.split(" ")[1])

    count_dict = collections.Counter(report_count_list)

    for report_val in report:
        [A, B] = report_val.split(" ")
        if count_dict[B]>=k:
            idx=id_list.index(A)
            answer[idx]=answer[idx]+1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
