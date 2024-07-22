"""
1-1. 50보다 크거나 같은지 확인
1-2. 짝수인지 확인 후 맞으면 2로 나눔
2-1. 1-1d의 elif 작으면 : 
2-2. 홀수이면 * 2
3. else : 그냥 출력
"""
def solution(arr):
    answer = []
    for i in arr :
        if i >= 50 :
            if i % 2 == 0 :
                answer.append(i/2)
            else : answer.append(i)
        elif i < 50 :
            if i % 2 != 0 :
                answer.append(i*2)
            else : 
                answer.append(i)
        else :
            answer.append(i)
                
    return answer

"""
def solution(arr):
    answer = []
    for i in arr:
        if i>=50 and i %2==0:
            answer.append(i/2)
        elif i<50 and i %2!=0:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer
"""