def solution(myString):
    answer = list(myString)
    for i in range(len(answer)) : 
        if 96 < ord(answer[i]) < 108 :
            answer[i] = 'l'
        
    answer = ''.join(answer)
            
    return answer

"""
def solution(myString):
    return ''.join(['l' if ord(i) < ord('l') else i for i in myString])
"""