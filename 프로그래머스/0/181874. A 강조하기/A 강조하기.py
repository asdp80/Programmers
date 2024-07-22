"""
1. 문자열 배열로 변환 후 순회
2-1. a일시, A로 변환
2-2. A일시, 그대로 저장
2-3. 그 외일시, 소문자로 변환
3. 문자열로 만든 후 출력
"""
def solution(myString):
    answer = ''
    for i in myString : 
        if i == 'a' :
            answer += 'A'
        elif i == 'A' :
            answer += i
        else :
            answer += i.lower()
    return answer