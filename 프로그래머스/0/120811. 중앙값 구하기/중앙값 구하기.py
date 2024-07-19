def solution(array):
    answer = 0
    array.sort()
    answer = len(array) // 2
    answer = array[answer]
    return answer