def solution(order):
    answer = list(str(order))
    count = 0
    for i in answer : 
        if int(i) == 3 or int(i) == 6 or int(i) == 9 :
            count += 1
    return count