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