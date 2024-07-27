"""
1. 1부터 곱한 것을 변수에 저장 후 카운트
2. 변수 > i일 때 시점일 때 break
3. 카운트 - 1 출력
"""

def solution(n):
    answer = 1
    count = 1
    while (answer <= n) : 
        answer *= count
        count += 1
    return count -2