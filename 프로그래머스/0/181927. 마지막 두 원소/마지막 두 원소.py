def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2] :
        answer.append(num_list[-1] - num_list[-2])
    elif  num_list[-2] >= num_list[-1] :
        answer.append(num_list[-1] * 2)
    
    return answer

"""
def solution(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    if n1 > n2:
        num_list.append(n1 - n2)
    else:
        num_list.append(n1 * 2)
    return num_list
"""