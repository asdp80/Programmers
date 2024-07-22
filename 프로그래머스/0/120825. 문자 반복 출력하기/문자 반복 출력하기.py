"""
1. 문자열 순회
2. 각 인덱스 * n 만큼 새로운 문자열에 저장
"""

def solution(my_string, n):
    answer = ''
    for i in my_string : 
        answer += i * n
    return answer