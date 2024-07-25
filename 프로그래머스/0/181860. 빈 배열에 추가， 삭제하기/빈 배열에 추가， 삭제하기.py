def solution(arr, flag):
    answer = []
    for i in range(len(arr)) :
        if flag[i] :
            answer.extend([arr[i]] * (arr[i] * 2))
        else :
            answer = answer[:-arr[i]]
    return list(answer)

"""
def solution(arr, flag):
    answer = []
    for a, f in zip(arr,flag):
        if f == False:
            answer = answer[:-a]
        else:
            answer += [a] * a*2
    return answer
"""