def solution(date1, date2):
    answer = 0
    for d1, d2 in zip(date1, date2) :
        if d1 > d2 :
            return 0
        elif d1 < d2 : return 1 
    return 0