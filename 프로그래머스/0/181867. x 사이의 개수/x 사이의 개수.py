def solution(myString):
    answer = []
    count = 0
    for i in myString : 
        if i != 'x' : 
            count += 1
        else : 
            answer.append(count)
            count = 0
    answer.append(count)
    return answer

"""
def solution(myString):
    return [len(w) for w in myString.split('x')]
"""