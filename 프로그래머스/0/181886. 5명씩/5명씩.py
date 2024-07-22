def solution(names):
    answer = []
    for i in names : 
        if (names.index(i)+1) % 5 == 1 :
            answer.append(i)
    return answer

"""
def solution(names):
    answer = []
    for i in range(0,len(names),5):
        answer.append(names[i])
    return answer
"""