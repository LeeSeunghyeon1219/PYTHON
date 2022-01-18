def cal_length(i, j):
    [x, y] = [int((i - 1) / 3), int((i - 1) % 3)]
    [x1, y1] = [int((j - 1) / 3), int((j - 1) % 3)]

    return abs(x1 - x) + abs(y1 - y)
def solution(numbers, hand):
    Left_hand = 10  # * 위치
    Right_hand = 12  # # 위치
    answer = ''
    print(Right_hand)

    for number in numbers:
        number = 11 if number == 0 else number

        if number in [1, 4, 7]:
            answer = answer + "L"
            Left_hand = number
        elif number in [3, 6, 9]:
            answer = answer + "R"
            Right_hand = number
        else:
            Left_length = cal_length(Left_hand, number)
            Right_length = cal_length(Right_hand, number)

            h_result = hand
            if Left_length < Right_length:
                h_result = "left"
            elif Left_length > Right_length:
                h_result = "right"

            if h_result=='left':
                answer = answer + "L"
                Left_hand=number
            else:
                answer=answer + "R"
                Right_hand = number
    return answer
