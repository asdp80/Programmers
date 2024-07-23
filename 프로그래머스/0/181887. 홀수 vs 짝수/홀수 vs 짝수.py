def solution(num_list):
    e, o = 0, 0
    for i in range(len(num_list)) : 
        if i % 2 == 0 :
            e += num_list[i]
        else : 
            o += num_list[i]
    
    return max(e,o)