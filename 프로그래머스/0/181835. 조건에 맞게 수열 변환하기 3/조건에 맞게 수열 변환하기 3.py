"""def solution(arr, k):
    answer = []
    for i in arr : 
        if k % 2 == 0 : 
            answer.append(i + k)
        else : 
            answer.append(i * k)
    return answer"""

def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]