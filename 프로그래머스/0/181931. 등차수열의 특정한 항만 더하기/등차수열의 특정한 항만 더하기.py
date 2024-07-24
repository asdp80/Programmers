def solution(a, d, included):
    answer = a
    result = 0
    for i in range(len(included)) :        
        if included[i] == 1 :
            result += answer
        answer += d
        
    return result