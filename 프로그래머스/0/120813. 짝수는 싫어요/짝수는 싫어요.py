"""
1. n이 짝수/홀수인지 판별한다.
2. 짝수라면, [1,n]까지 2의 간격으로 새 배열 변수에 append 해준다.
3. 홀수라면, [1,n+1]까지 2의 간격으로 새 배열 변수에 append 해준다.

"""


def solution(n):
    answer = []
    if n % 2 == 0 : 
        for i in range(1, n, 2) :
            answer.append(i)
    else :
        for i in range(1, n+1, 2) :
            answer.append(i)
        
    return answer