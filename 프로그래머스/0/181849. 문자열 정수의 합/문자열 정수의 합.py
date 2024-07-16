def solution(num_str):
    answer = 0
    for char in num_str:
        answer += int(char)  # 각 문자를 정수로 변환하여 더하기
    return answer