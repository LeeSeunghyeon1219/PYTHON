## BaekJoon 1157번 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지
# 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력: 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 모두 1,000,000을 넘지 않음
# 출력: 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

import collections

input_str=str(input().upper())
input_dict=collections.Counter(input_str)
max_value=max(list(input_dict.values()))

MAX_VAL=""
MAX_VALUE_COUNT=0
for i in list(input_dict.keys()):
    if max_value==input_dict[i]:
        MAX_VALUE_COUNT=MAX_VALUE_COUNT+1
        MAX_VAL=i
if MAX_VALUE_COUNT>1:
    print("?")
else:
    print(MAX_VAL)
