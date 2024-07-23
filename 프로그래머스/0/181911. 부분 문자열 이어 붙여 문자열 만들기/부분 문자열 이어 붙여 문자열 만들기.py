"""
1. parts 길이만큼 순회
2. my_string[i]의 s-e 문자열 answer에 저장

"""
def solution(my_strings, parts):
    answer = []
    for i in range(0, len(parts)) : 
        s, e = parts[i]        
        answer.append(my_strings[i][s:e+1])
    answer = ''.join(answer)
    return answer