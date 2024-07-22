"""
1. 문자열 배열로 바꾸기
2. 인덱스 두개 스왑
3. 배열 문자열로 변환
4. 출력
"""

def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1], answer[num2] = answer[num2], answer[num1]
     
    return ''.join(answer)