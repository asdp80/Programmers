def solution(sides):
    answer = sorted(sides)
    return 1 if answer[2] < answer[0] + answer[1] else 2