def solution(my_string):
    answer = ''
    for i in range(1, len(my_string)+1):
        answer += my_string[-i]
    return answer

"""
def solution(my_string):
    return my_string[::-1]
"""