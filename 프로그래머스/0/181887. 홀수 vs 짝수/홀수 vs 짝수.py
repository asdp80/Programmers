def solution(num_list):
    e, o = 0, 0
    for i in range(len(num_list)) : 
        if i % 2 == 0 :
            e += num_list[i]
        else : 
            o += num_list[i]
    
    return max(e,o)

"""
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
"""