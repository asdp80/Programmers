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
"""
def solution(my_string, m, c):
    answer = ''
    
    # 문자열을 m 글자씩 나누어 2차원 배열로 변환
    for i in range(0, len(my_string), m):
        answer += my_string[i:i+m][c-1]
    
    return answer
"""
"""
def solution(s, m, c):
    return s[c-1::m]
"""