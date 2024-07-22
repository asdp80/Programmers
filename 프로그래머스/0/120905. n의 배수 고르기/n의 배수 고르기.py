"""
1. 배열 순회
2. n의 배수가 맞으면 answer에 저장
3. 출력
"""
def solution(n, numlist):
    answer = []
    for i in numlist :
        if i % n == 0 :
            answer.append(i)
        
    return answer