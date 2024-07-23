def solution(my_string):
    answer = my_string.lower()
    answer = sorted(answer)
    
    return ''.join(answer)

"""
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

"""