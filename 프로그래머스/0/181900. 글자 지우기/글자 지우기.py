def solution(my_string, indices):
    answer = list(my_string)
    result = []
    for i in range(len(answer)) : 
        if i not in indices : 
            result.append(answer[i])
        
    return ''.join(result)