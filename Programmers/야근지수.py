def solution(n, works):
    answer = 0

    if n >= sum(works):
        return 0

    works.sort()
    for _ in range(n):
        works[-1] -= 1
        works.sort()

    for w in works:
        answer += w ** 2
    return answer


import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    answer = 0
    for w in works:
        answer += w ** 2
    return answer
