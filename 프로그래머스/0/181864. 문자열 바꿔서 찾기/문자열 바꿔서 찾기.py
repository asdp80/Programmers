"""
1. 문자열 2개 입력
2. s1의 문자열 반대로 치환
2-1 배열로 변환
2-2 치환
2-3 다시 문자열로 변환
3. s2 in s1 -> return 1 / 0
"""

def solution(myString, pat):
    conv = list(myString)
    
    for i in range(len(conv)) :
        if conv[i] == 'A' :
            conv[i] = 'B'
        else :
            conv[i] = 'A'
    conv = ''.join(conv)
    
    if pat in conv :
        return 1
    else :
        return 0
    
