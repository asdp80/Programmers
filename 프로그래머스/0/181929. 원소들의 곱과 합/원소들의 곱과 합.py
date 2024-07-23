def solution(num_list):
    answer = 1
    a = sum(num_list) ** 2
    for i in num_list :
        answer *= i
        
    return 1 if answer < a else 0

"""
def solution(num_list):
    mul = 1 
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)
"""