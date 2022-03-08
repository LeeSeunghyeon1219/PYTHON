## 예시1 - 팩토리얼 재귀함수로 구현하기
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)
print(recursive_factorial(5))