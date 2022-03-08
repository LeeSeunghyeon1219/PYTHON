## 예시4 - 최대공약수(유클리드호제법) 재귀함수로 구현하기
#1. 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자
#2. 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다

def gcb(a,b):
    if a%b==0:
        return b
    else:
        return gcb(b,a%b)

print(gcb(12,8))
