def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n) :
        for j in range(0,n) :
            if i == j :
                answer[i][j] = 1
    return answer