def solution(emergency):
    # 응급도 리스트를 정렬하여 결과를 얻습니다.
    sorted_emergency = sorted(emergency, reverse=True)
    
    # 순위를 저장할 리스트를 만듭니다.
    answer = [0] * len(emergency)
    
    # 각 원소의 순위를 결정합니다.
    for i, value in enumerate(emergency):
        rank = sorted_emergency.index(value) + 1
        answer[i] = rank
    
    return answer
