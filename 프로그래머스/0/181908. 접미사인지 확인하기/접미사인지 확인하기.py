def solution(my_string, is_suffix):
    answer = 0
    return 1 if my_string.endswith(is_suffix) else 0

"""
def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0
"""