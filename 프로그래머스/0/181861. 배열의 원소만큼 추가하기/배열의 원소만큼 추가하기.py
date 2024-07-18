"""
1. 빈 배열 x
2. arr의 크기만큼 loop
3. 원소의 크기만큼 loop
4. 빈 배열에 원소의 크기만큼 원소 추가하기
"""
def solution(arr):
    answer = []
    for i in range(len(arr)):
        for _ in range(arr[i]):
            answer.append(arr[i])
    return answer