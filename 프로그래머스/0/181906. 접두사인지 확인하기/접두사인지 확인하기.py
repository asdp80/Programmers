def solution(my_string, is_prefix):
    # 'is_prefix'가 'my_string'의 접두사인지 확인
    if len(is_prefix) > len(my_string):
        return 0
    
    for i in range(len(is_prefix)):
        if my_string[i] != is_prefix[i]:
            return 0
    return 1