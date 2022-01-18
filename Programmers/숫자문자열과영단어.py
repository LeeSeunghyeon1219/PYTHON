def solution(s):
    answer = 0

    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,'nine': 9}
    answer_str = ''

    val_str = ""
    for val in s:

        if val.isnumeric():
            answer_str = answer_str + val
            continue
        val_str = val_str + val
        if val_str in num_dict.keys():
            answer_str = answer_str + str(num_dict[val_str])
            val_str=""

    answer=int(answer_str)
    return answer
print(solution("one4seveneight"))


####

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
