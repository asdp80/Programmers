def solution(n):
    #answer = map(int ,reversed(sorted(list(str(n)))))
    answer = sorted(str(n))[::-1]
    answer = int(''.join(answer))
    return answer