"""
1. 배열 순회
2. 전 인덱스와 다음 인덱스의 값 비교
3. 큰 수 변수에 저장, 인덱스도 다른 변수에 저장
4. 출력
"""

def solution(array):
    a, b = 0, 0
    answer = []
    for i in range(0, len(array)-1) :
        if array[i] > array[i+1] :
            a = array[i]
            b = i
        else :
            a = array[i+1]
            b = i+1
    answer.append(a)
    answer.append(b)
    
    return answer

"""
def solution(array):
    return [max(array), array.index(max(array))]
"""