def solution(my_string, s, e):
    answer = my_string[s:e+1]
    answer = answer[::-1]
    result = my_string[:s] + answer + my_string[e+1:]
    return result