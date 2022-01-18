def solution(new_id):
    answer = ''
    # 1단계
    new_id=new_id.lower()
    # 2단계
    for val in new_id:
        if val.isalnum() or val in '-._':
            answer=answer+val
    # 3단계
    while ".." in answer:
        answer=answer.replace("..",".")

    #4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' and len(answer)>0 else answer

    # 5단계
    answer = 'a' if answer=="" else answer

    #6단계
    if len(answer)>15:
        answer=answer[:15]
        if answer[-1]==".":
            answer=answer[:-1]

    # 7단계
    if len(answer)<=2:
        answer = answer + answer[-1] * (3-len(answer))

    return answer

#############################################################
from re import sub


def solution(new_id):
    new_id = new_id.lower()
    new_id = sub("[^a-z0-9-_.]", "", new_id)
    new_id = sub("\.+", ".", new_id)
    new_id = sub("(^\.|\.$)", "", new_id)
    new_id = new_id if new_id else "a"
    new_id = sub("\.$", "", new_id[:15])
    new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id
