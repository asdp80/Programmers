"""
2중 for문 
1. s1 배열을 기준으로 s2 배열 순회
2. 같을 시, 변수에 += 1
"""
def solution(s1, s2):
    answer = 0

    for i in s1 : 
        for j in s2 :
            if i == j :
                answer += 1                
    return answer