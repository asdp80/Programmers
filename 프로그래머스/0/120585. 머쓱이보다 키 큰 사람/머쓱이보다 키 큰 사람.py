"""
1. 키 큰 사람 수 카운트할 변수 선언
2. 학생들 키 순차 출력
3. 머쓱이와 키 비교
4. 학생 키가 더 클 시, 변수 += 1
5. 출력
"""
def solution(array, height):
    answer = 0
    for i in array : 
        if i > height :
            answer += 1
    return answer