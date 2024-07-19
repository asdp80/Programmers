def solution(money):
    answer = []
    cnt , remain = money // 5500, money % 5500
    answer.append(cnt)
    answer.append(remain)
    
    return answer