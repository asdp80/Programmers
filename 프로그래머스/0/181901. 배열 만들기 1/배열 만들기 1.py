def solution(n, k):
    answer = []
    a = 1
    while (n >= k*a) :
        answer.append(k*a)
        a+= 1
    return answer