"""def solution(my_string):
    answer = ''.join(set(my_string))
    return answer"""

def solution(my_string):
    seen = set()  # 이미 추가된 문자를 추적하는 집합
    result = []  # 순서대로 문자들을 저장할 리스트
    
    for char in my_string:
        if char not in seen:  # 문자가 집합에 없으면
            seen.add(char)  # 집합에 문자를 추가
            result.append(char)  # 결과 리스트에 문자를 추가
    
    return ''.join(result)  # 리스트를 문자열로 변환하여 반환
