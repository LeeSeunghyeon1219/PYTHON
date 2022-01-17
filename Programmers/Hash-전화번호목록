def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):

        if i == len(phone_book) - 1:
            break
        if phone_book[i] == phone_book[i + 1][:len(phone_book)]:
            answer = False
            break
    return answer

print(solution(["12","123","1235","567","88"]))
