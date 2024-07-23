def solution(n, k):
    answer = []
    a = 1
    while (n >= k*a) :
        answer.append(k*a)
        a+= 1
    return answer

"""
def solution(n, k):
    answer = []

    for i in range(k, n+1, k):
        answer.append(i)

    return answer
"""