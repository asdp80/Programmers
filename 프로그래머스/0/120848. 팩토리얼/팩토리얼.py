

def solution(n):
    answer = 1
    count = 1
    while (answer <= n) : 
        answer *= count
        count += 1
    return count -2