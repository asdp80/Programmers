"""
1. 문자열 2차원 배열로 변환
2. 
"""
def solution(my_string, m, c):
    answer = []
    result = ''
    for i in range(0, len(my_string), m) : 
            answer.append(my_string[i:i+m])
    
    for i in range(len(answer)) :
        result += answer[i][c-1]
    
    return result