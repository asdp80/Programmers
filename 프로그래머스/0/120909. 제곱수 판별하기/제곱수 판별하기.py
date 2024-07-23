import math 
def solution(n):
    answer = math.sqrt(n)
    return 1 if answer == int(answer) else 2

"""
def solution(n):
    for i in range(1,n):
        if n == i * i:
            return 1
    return 2
"""