def solution(num, k):
    answer = list(str(num))
    count = 0
    for i in range(0, len(answer)) :
        if int(answer[i]) == k :
            return i+1
    return -1