def solution(names):
    answer = []
    for i in names : 
        if (names.index(i)+1) % 5 == 1 :
            answer.append(i)
    return answer