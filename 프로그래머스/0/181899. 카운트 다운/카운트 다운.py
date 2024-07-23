"""
1. s_num부터 저장
2. s_num -= 1
3. if s_num == e_num
4. return
"""
def solution(start_num, end_num):
    answer = []
    while(start_num >= end_num) :
        answer.append(start_num)
        start_num -= 1
    return answer