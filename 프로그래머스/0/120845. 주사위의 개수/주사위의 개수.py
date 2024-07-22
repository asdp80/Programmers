"""
1. (가로 // n) * (세로 // n) 을 변수에 저장
2. answer = 1 저장한 변수 * (높이 // n)
"""

def solution(box, n):
    answer = 0
    
    sq = (box[0] // n) * (box[1] // n)
    answer = sq * (box[2] // n)
    return answer