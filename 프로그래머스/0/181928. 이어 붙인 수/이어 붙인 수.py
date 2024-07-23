def solution(num_list):
    answer = 0
    e, o = '',''
    for i in num_list :
        if i % 2 == 0 :
            e += str(i)
        else :
            o += str(i)
    answer = int(e) + int(o)
    return answer