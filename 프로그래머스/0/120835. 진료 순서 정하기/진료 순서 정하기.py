"""
1. 높은 순 정렬
2. 정렬한 것과 원래 emergency 비교해서 같은 값 인덱스 + 1 저장
"""

def solution(emergency):
    answer = sorted(emergency, reverse = True)
    result = [] 
    for i in emergency : 
            result.append(answer.index(i) + 1)
    
    return result
"""
def solution(emergency):
    arr = []
    for i in emergency:
        idx = 1
        for j in emergency:
            if i < j:
                idx += 1
        arr.append(idx)
    return arr
"""
"""
def solution(emergency):
    sort = sorted(emergency, reverse=True)
    return [sort.index(i) + 1 for i in emergency]
"""


