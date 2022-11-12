def solution(numbers, target):
    answer = 0

    def dfs(num, idx):
        if len(numbers) == idx:
            if target == num:
                nonlocal answer
                answer += 1
        else:
            n = numbers[idx]
            idx += 1
            dfs(num + n, idx)
            dfs(num - n, idx)

    dfs(0, 0)

    return answer

from collections import deque

def solution(numbers, target):
    answer = 0

    ### bfs 로 구현하기
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


from collections import deque


def solution(numbers, target):
    answer = 0

    ### bfs 로 구현하기
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
