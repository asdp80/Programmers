def solution(a, b):
    answer = 0
    if a <= b :
        for i in range(a, b+1) :
            answer += i
    else : 
        for i in range(b, a+1) :
            answer += i
    return answer

"""
def adder(a, b):
    return sum(range(min(a, b), max(a, b)+1))

def solution(a, b):
    return sum(range(a,b+1) if a <= b else range(b,a+1))
"""