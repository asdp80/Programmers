def solution(arr, divisor):
    answer = []
    for i in arr : 
        if i % divisor == 0 :
            answer.append(i)
    if answer == [] :
        answer.append(-1)
    
    return sorted(answer)

"""
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];
"""