def solution(n):
    answer = 0
    while(n>0):
        if n % 2 == 0 :
            answer +=n
            n-=2
        else :
            n = n-1
            answer += n
            n -=1
    return answer

"""
def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer
"""