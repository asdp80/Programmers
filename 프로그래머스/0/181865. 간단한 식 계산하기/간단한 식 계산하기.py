"""
1. 문자열 쪼개기
2. [0] , [2] 숫자로 변환

"""

def solution(binomial):
    answer = binomial.split()
    result = 0
    if answer[1] == '+' :
        result = float(answer[0]) + float(answer[2])
    elif answer[1] == '-' :
        result = float(answer[0]) - float(answer[2])
    elif answer[1] == '*' :
        result = float(answer[0]) * float(answer[2])
    return result