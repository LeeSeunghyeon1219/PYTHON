def solution(msg):
    dict_list = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    print(dict_list)

    data_list = []
    idx = 0
    start = 0
    end=1
    while start!=end:
        if end>len(msg):
            break
        find_data=msg[start:end]
        while find_data in dict_list:
            if end>len(msg):
                break
            if find_data=="":
                break
            idx=dict_list.index(find_data)+1
            end=end+1
            find_data=msg[start:end]
        dict_list.append(find_data)
        if find_data=="":
            idx=dict_list.index(find_data)+1
            data_list.append(idx)
            break
        start=end-1
        end=start+1
        data_list.append(idx)

    print(dict_list)
    return data_list

print(solution("KAKAO"))

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
