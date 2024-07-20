"""
1. 문자열 code 간격으로 for문
2. 빈 배열에 append
3. 배열 출력
"""

def solution(cipher, code):
    answer = []
    for i in range(code-1, len(cipher), code) :
            answer.append(cipher[i])
    
    result = ''.join(answer)
    
    return result